from collective.cart.stock.schema import StockSchema
from plone.dexterity.interfaces import IDexterityContainer
from zope.interface import Attribute


class IStock(IDexterityContainer, StockSchema):
    """Interface for content type: collective.cart.stock.Stock"""

    initial_stock = Attribute('Initial stock')
