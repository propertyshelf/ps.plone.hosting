# -*- coding: utf-8 -*-
"""The `Directory` is the root for the hosting management."""

# zope imports
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class IDirectory(model.Schema):
    """Interface for Directory content type."""


@implementer(IDirectory)
class Directory(Container):
    """Directory content type"""
