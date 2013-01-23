from collective.cart.stock import _
from plone.directives import form
from zope.schema import Int


class IStock(form.Schema):
    """Interface for collective.cart.stock.Stock dexterity content type."""

    stock = Int(
        title=_('Stock'),
        description=_('Set the initial stock here.'))
