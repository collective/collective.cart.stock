from collective.cart.stock.interfaces import IStock
from plone.dexterity.content import Container
from zope.interface import implements


class Stock(Container):
    """Content type: collective.cart.stock.Stock"""
    implements(IStock)

    stock = None
    initial_stock = None
