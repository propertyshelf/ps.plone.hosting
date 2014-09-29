# -*- coding: utf-8 -*-
"""A `Domain`."""

# python imports
import datetime

# zope imports
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.formwidget.datetime.z3cform import DateWidget
from plone.supermodel import model
from z3c.form.widget import FieldWidget
from zope import schema
from zope.interface import implementer

# local imports
from ps.plone.hosting import _


def DateFieldWidget(field, request):
    """IFieldWidget factory for DatetimeWidget."""
    widget = FieldWidget(field, DateWidget(request))
    currentYear = datetime.date.today().year
    # Don't display dates before 1985 (first domain registration).
    minimumYearRange = currentYear - 1985
    widget.years_range = (-minimumYearRange, 1)
    return widget


class IDomain(model.Schema):
    """Interface for the `Domain` content type."""

    title = schema.TextLine(
        required=True,
        title=_(u'Domain Name')
    )

    external_hosted = schema.Bool(
        description=_(u'Is this domain hosted by another registrar?'),
        required=False,
        title=(u'External Hosted Domain'),
    )

    external_managed = schema.Bool(
        description=_(u'Is this domain managed by another domain server?'),
        required=False,
        title=(u'External Domain Management'),
    )

    external_dns = schema.List(
        description=_(u'List of external DNS servers.'),
        required=False,
        title=_(u'External DNS servers'),
        value_type=schema.TextLine(
            title=_(u'DNS Server'),
        ),
    )

    directives.widget(registration_date=DateFieldWidget)
    registration_date = schema.Date(
        required=True,
        title=_(u'Registration Date'),
    )


@implementer(IDomain)
class Domain(Container):
    """`Domain` content type."""
