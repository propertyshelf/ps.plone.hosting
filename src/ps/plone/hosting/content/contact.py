# -*- coding: utf-8 -*-
"""A `Contact` can represent a `Customer`."""

# zope imports
from plone.dexterity.content import Item
from plone.supermodel import model
from zope import schema
from zope.interface import implementer

# local imports
from ps.plone.hosting import _


class IContact(model.Schema):
    """Interface for the `Contact` content type."""

    title = schema.TextLine(
        required=True,
        title=_(u'Display Name')
    )


@implementer(IContact)
class Contact(Item):
    """`Contact` content type."""
