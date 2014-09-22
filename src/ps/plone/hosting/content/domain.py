# -*- coding: utf-8 -*-
"""A `Domain`."""

# zope imports
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer

# local imports
from ps.plone.hosting import _


class IDomain(model.Schema):
    """Interface for the `Domain` content type."""

    title = schema.TextLine(
        required=True,
        title=_(u'Domain Name')
    )


@implementer(IDomain)
class Domain(Container):
    """`Domain` content type."""
