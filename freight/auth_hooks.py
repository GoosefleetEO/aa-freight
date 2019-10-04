from allianceauth.services.hooks import MenuItemHook, UrlHook
from django.utils.translation import ugettext_lazy as _
from allianceauth import hooks
from . import urls


class ExampleMenuItem(MenuItemHook):
    """ This class ensures only authorized users will see the menu entry """
    def __init__(self):
        # setup menu entry for sidebar
        MenuItemHook.__init__(
            self,
            _('Alliance Freight'),
            'fa fa-truck fa-fw',
            'freight:index',
            navactive=['freight:index']
        )

    def render(self, request):
        if request.user.has_perm('freight.basic_access'):
            return MenuItemHook.render(self, request)
        return ''


@hooks.register('menu_item_hook')
def register_menu():
    return ExampleMenuItem()


@hooks.register('url_hook')
def register_urls():
    return UrlHook(urls, 'freight', r'^freight/')