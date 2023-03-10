from celery import chain, shared_task

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from allianceauth.services.hooks import get_extension_logger
from app_utils.logging import LoggerAddTag

from . import __title__
from .models import Contract, ContractHandler, Location

logger = LoggerAddTag(get_extension_logger(__name__), __title__)


def _get_user(user_pk) -> User:
    """returns the user or None. Logs if user is requested but can't be found."""
    user = None
    if user_pk:
        try:
            user = User.objects.get(pk=user_pk)
        except User.DoesNotExist:
            logger.warning("Ignoring non-existing user with pk %s", user_pk)
    return user


def _get_contract_handler() -> ContractHandler:
    handler = ContractHandler.objects.first()
    if not handler:
        logger.warning("No contract handler was found")
        raise ObjectDoesNotExist()
    return handler


@shared_task
def update_contracts_esi(force_sync=False, user_pk=None) -> None:
    """start syncing contracts"""
    _get_contract_handler().update_contracts_esi(force_sync, user=_get_user(user_pk))


@shared_task
def send_contract_notifications(force_sent=False, rate_limited=True) -> None:
    """Send notification about outstanding contracts that have pricing"""
    Contract.objects.send_notifications(force_sent, rate_limited)


@shared_task
def run_contracts_sync(force_sync=False, user_pk=None) -> None:
    """main task coordinating contract sync"""
    my_chain = chain(
        update_contracts_esi.si(force_sync, user_pk), send_contract_notifications.si()
    )
    my_chain.delay()


@shared_task
def update_contracts_pricing() -> int:
    """Updates pricing for all contracts"""
    update_count = Contract.objects.filter_not_completed().update_pricing()
    logger.info("Updated pricing for %s contracts", update_count)
    return update_count


@shared_task
def update_location(location_id: int) -> None:
    """Updates the location from ESI"""
    Location.objects.get(id=location_id)
    token = _get_contract_handler().token()
    Location.objects.update_or_create_esi(location_id=location_id, token=token)


@shared_task
def update_locations(location_ids: list) -> None:
    """Updates the locations from ESI"""
    for location_id in location_ids:
        update_location.delay(location_id)
