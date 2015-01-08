# -*- coding: utf-8 -*-
"""A `Hosting` of a web service."""

# zope imports
from collective.z3cform.datetimewidget import DateWidget
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.supermodel import model
from z3c.form.widget import FieldWidget
from z3c.relationfield.schema import RelationList
from zope import schema
from zope.interface import implementer

# local imports
from ps.plone.hosting import _


def DateFieldWidget(field, request):
    """IFieldWidget factory for DatetimeWidget."""
    widget = FieldWidget(field, DateWidget(request))
    widget.show_jquerytools_dateinput = True
    widget.show_today_link = True
    return widget


class IHosting(model.Schema):
    """Interface for the `Hosting` content type."""

    title = schema.TextLine(
        required=True,
        title=_(u'Hosting Display Name')
    )

    hosting_type = schema.Choice(
        required=True,
        title=_(u'Type of Hosting'),
        values=['plone_shared', 'plone_professional', 'mls', ]
    )

    directives.widget(service_start=DateFieldWidget)
    service_start = schema.Date(
        required=True,
        title=_(u'Start Date'),
    )

    hosting_url = schema.TextLine(
        required=False,
        title=_(u'Hosting URL'),
    )

    management_url = schema.TextLine(
        required=False,
        title=_(u'Management URL'),
    )

    description = schema.Text(
        required=False,
        title=_(u'Description'),
    )

    domains = RelationList(
        description=_(
            u'Search and attach domains connected to this hosting service.'
        ),
        required=False,
        title=_('Domains'),
        value_type=schema.Choice(
            source=ObjPathSourceBinder(
                portal_type=[
                    'ps.plone.hosting.domain',
                    'ps.plone.hosting.externaldomain',
                ],
            ),
        ),
    )


@implementer(IHosting)
class Hosting(Container):
    """`Hosting` content type."""
