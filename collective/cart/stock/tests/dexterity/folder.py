from five import grok
from plone.directives import form


class ICFolder(form.Schema):
    """Container for Testing."""


class View(grok.View):
    """Default view for page."""

    grok.context(ICFolder)
    grok.require('zope2.View')
    grok.name('view')
