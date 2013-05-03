from collective.cart.stock.content import Stock
from collective.cart.stock.interfaces import IStock
from plone.dexterity.content import Container
from plone.dexterity.interfaces import IDexterityContainer
from zope.interface.verify import verifyObject

import unittest


class StockTestCase(unittest.TestCase):
    """TestCase for content type: collective.cart.stock.Stock"""

    def test_subclass(self):
        from collective.cart.stock.schema import StockSchema
        self.assertTrue(issubclass(Stock, Container))
        self.assertTrue(issubclass(IStock, (StockSchema, IDexterityContainer)))

    def test_instance__verifyObject(self):
        self.assertTrue(verifyObject(IStock, Stock()))
