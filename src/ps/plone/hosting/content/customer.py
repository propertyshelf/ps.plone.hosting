# -*- coding: utf-8 -*-
"""A `Customer` can have multiple hostings, like domains and web services."""

# zope imports
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class ICustomer(model.Schema):
    """Interface for the `Customer` content type."""


@implementer(ICustomer)
class Customer(Container):
    """`Customer` content type."""
