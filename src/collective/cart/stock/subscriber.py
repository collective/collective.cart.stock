from collective.cart.stock.interfaces import IStock
from five import grok
from zope.lifecycleevent.interfaces import IObjectCreatedEvent

import logging


logger = logging.getLogger(__name__)


@grok.subscribe(IStock, IObjectCreatedEvent)
def set_initial_stock(context, event):
    setattr(context, 'initial_stock', context.stock)
    message = 'Set initial_stock to {}'.format(context.stock)
    logger.info(message)
