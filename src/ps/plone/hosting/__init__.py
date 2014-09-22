# -*- coding: utf-8 -*-
"""Propertyshelf Hosting Management."""

# zope imports
from zope.i18nmessageid import MessageFactory


_ = MessageFactory('ps.plone.hosting')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
