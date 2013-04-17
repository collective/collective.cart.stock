from collective.cart.stock.interfaces import IStock
from zope.component import adapter
from zope.lifecycleevent.interfaces import IObjectCreatedEvent

import logging


logger = logging.getLogger(__name__)


@adapter(IStock, IObjectCreatedEvent)
def set_initial_stock(context, event):
    setattr(context, 'initial_stock', context.stock)
    message = 'Set initial_stock to {}'.format(context.stock)
    logger.info(message)
