# -*- coding: utf-8 -*-
"""A `Customer` can have multiple hostings, like domains and web services."""

# zope imports
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer

# local imports
from ps.plone.hosting import _


class ICustomer(model.Schema):
    """Interface for the `Customer` content type."""

    title = schema.TextLine(
        required=True,
        title=_(u'Display Name')
    )


@implementer(ICustomer)
class Customer(Container):
    """`Customer` content type."""
