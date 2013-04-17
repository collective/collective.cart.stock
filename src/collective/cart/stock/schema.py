from collective.cart.stock import _
from plone.supermodel.model import Schema
from zope import schema


class StockSchema(Schema):
    """Schema for content type: collective.cart.stock.Stock"""

    stock = schema.Int(
        title=_('Stock'),
        description=_('Set the initial stock here.'))
