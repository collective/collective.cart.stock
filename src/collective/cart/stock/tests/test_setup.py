from Products.CMFCore.utils import getToolByName
from collective.cart.stock.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_sll_stock_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('collective.cart.stock'))

    def test_installed__plone_app_dexterity(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('plone.app.dexterity'))

    def test_browserlayer(self):
        from collective.cart.stock.browser.interfaces import ICollectiveCartStockLayer
        from plone.browserlayer import utils
        self.failUnless(ICollectiveCartStockLayer in utils.registered_layers())

    def test_rolemap__collective_cart_stock_AddStock__rolesOfPermission(self):
        permission = "collective.cart.stock: Add Stock"
        roles = [
            item['name'] for item in self.portal.rolesOfPermission(
                permission
            ) if item['selected'] == 'SELECTED'
        ]
        roles.sort()
        self.assertEqual(
            roles,
            [
                'Contributor',
                'Manager',
                'Owner',
                'Site Administrator',
            ]
        )

    def test_rolemap__collective_cart_stock_AddStock__acquiredRolesAreUsedBy(self):
        permission = "collective.cart.stock: Add Stock"
        self.assertEqual(
            self.portal.acquiredRolesAreUsedBy(permission),
            'CHECKED'
        )

    def test_types__collective_cart_stock_Stock__i18n_domain(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        self.assertEqual(ctype.i18n_domain, 'collective.cart.stock')

    def test_types__collective_cart_stock_Stock__meta_type(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        self.assertEqual(ctype.meta_type, 'Dexterity FTI')

    def test_types__collective_cart_stock_Stock__title(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        self.assertEqual(ctype.title, 'Stock')

    def test_types__collective_cart_stock_Stock__description(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        self.assertEqual(ctype.description, '')

    def test_types__collective_cart_stock_Stock__content_icon(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        self.assertEqual(ctype.getIcon(), '++resource++collective.cart.stock/stock.png')

    def test_types__collective_cart_stock_Stock__allow_discussion(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        self.assertFalse(ctype.allow_discussion)

    def test_types__collective_cart_stock_Stock__global_allow(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        self.assertFalse(ctype.global_allow)

    def test_types__collective_cart_stock_Stock__filter_content_types(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        self.assertTrue(ctype.filter_content_types)

    def test_types__collective_cart_stock_Stock__allowed_content_types(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        self.assertEqual(ctype.allowed_content_types, ())

    def test_types__collective_cart_stock_Stock__schema(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        self.assertEqual(ctype.schema, 'collective.cart.stock.interfaces.IStock')

    def test_types__collective_cart_stock_Stock__klass(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        self.assertEqual(ctype.klass, 'plone.dexterity.content.Container')

    def test_types__collective_cart_stock_Stock__add_permission(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        self.assertEqual(ctype.add_permission, 'collective.cart.stock.AddStock')

    def test_types__collective_cart_stock_Stock__behaviors(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        self.assertEqual(
            ctype.behaviors,
            ('plone.app.dexterity.behaviors.metadata.IBasic',))

    def test_types__collective_cart_stock_Stock__default_view(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        self.assertEqual(ctype.default_view, 'view')

    def test_types__collective_cart_stock_Stock__default_view_fallback(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        self.assertFalse(ctype.default_view_fallback)

    def test_types__collective_cart_stock_Stock__view_methods(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        self.assertEqual(ctype.view_methods, ('view',))

    def test_types__collective_cart_stock_Stock__default_aliases(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        self.assertEqual(
            ctype.default_aliases,
            {'edit': '@@edit', 'sharing': '@@sharing', '(Default)': '(dynamic view)', 'view': '(selected layout)'})

    def test_types__collective_cart_stock_Stock__action__view__title(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.title, 'View')

    def test_types__collective_cart_stock_Stock__action__view__condition(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.condition, '')

    def test_types__collective_cart_stock_Stock__action__view__url_expr(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.getActionExpression(), 'string:${folder_url}/')

    def test_types__collective_cart_stock_Stock__action__view__visible(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        action = ctype.getActionObject('object/view')
        self.assertTrue(action.visible)

    def test_types__collective_cart_stock_Stock__action__view__permissions(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.permissions, (u'Modify portal content',))

    def test_types__collective_cart_stock_Stock__action__edit__title(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.title, 'Edit')

    def test_types__collective_cart_stock_Stock__action__edit__condition(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.condition, '')

    def test_types__collective_cart_stock_Stock__action__edit__url_expr(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.getActionExpression(), 'string:${object_url}/edit')

    def test_types__collective_cart_stock_Stock__action__edit__visible(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        action = ctype.getActionObject('object/edit')
        self.assertTrue(action.visible)

    def test_types__collective_cart_stock_Stock__action__edit__permissions(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('collective.cart.stock.Stock')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.permissions, (u'Modify portal content',))

    def test_workflow__context_cart_stock_Stock(self):
        workflow = getToolByName(self.portal, 'portal_workflow')
        self.assertEqual(workflow.getChainForPortalType('collective.cart.stock.Stock'), ())

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.cart.stock'])
        self.failIf(installer.isProductInstalled('collective.cart.stock'))

    def test_uninstall__browserlayer(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.cart.stock'])
        from collective.cart.stock.browser.interfaces import ICollectiveCartStockLayer
        from plone.browserlayer import utils
        self.failIf(ICollectiveCartStockLayer in utils.registered_layers())
