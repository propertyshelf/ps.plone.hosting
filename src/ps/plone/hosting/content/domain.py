# -*- coding: utf-8 -*-
"""A `Domain`."""

# python imports
import datetime

# zope imports
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.formwidget.datetime.z3cform import DateWidget
from plone.formwidget.masterselect import MasterSelectBoolField
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form.widget import FieldWidget
from z3c.relationfield.schema import RelationChoice
from zope import schema
from zope.interface import implementer

# local imports
from ps.plone.hosting import _


DOMAIN_CONTATCS_FIELDS = (
    'owner_c',
    'admin_c',
    'tech_c',
    'zone_c',
)


def DateFieldWidget(field, request):
    """IFieldWidget factory for DatetimeWidget."""
    widget = FieldWidget(field, DateWidget(request))
    currentYear = datetime.date.today().year
    # Don't display dates before 1985 (first domain registration).
    minimumYearRange = currentYear - 1985
    widget.years_range = (-minimumYearRange, 1)
    return widget


class IExternalDomain(model.Schema):
    """Interface for the `External Domain` content type."""

    title = schema.TextLine(
        required=True,
        title=_(u'Domain Name')
    )


class IDomain(model.Schema):
    """Interface for the `Domain` content type."""

    fieldset(
        'domain_contacts',
        label=_(u'Domain Contacts'),
        fields=DOMAIN_CONTATCS_FIELDS,
    )

    title = schema.TextLine(
        required=True,
        title=_(u'Domain Name')
    )

    external_managed = MasterSelectBoolField(
        description=_(u'Is this domain managed by another domain server?'),
        required=False,
        slave_fields=(
            {
                'masterID': 'form-widgets-external_managed-0',
                'name': 'external_dns',
                'action': 'show',
                'hide_values': 1,
                'siblings': True,
            },
        ),
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

    owner_c = RelationChoice(
        description=_(u'Domain owner.'),
        required=False,
        source=ObjPathSourceBinder(
            portal_type=[
                'ps.plone.hosting.contact',
                'ps.plone.hosting.customer',
            ],
        ),
        title=_(u'Owner-C'),
    )

    admin_c = RelationChoice(
        description=_(u'Domain admin.'),
        required=False,
        source=ObjPathSourceBinder(
            portal_type=[
                'ps.plone.hosting.contact',
                'ps.plone.hosting.customer',
            ],
        ),
        title=_(u'Admin-C'),
    )

    tech_c = RelationChoice(
        description=_(u'Technical domain contact.'),
        required=False,
        source=ObjPathSourceBinder(
            portal_type=[
                'ps.plone.hosting.contact',
                'ps.plone.hosting.customer',
            ],
        ),
        title=_(u'Tech-C'),
    )

    zone_c = RelationChoice(
        description=_(u'Zone domain contact.'),
        required=False,
        source=ObjPathSourceBinder(
            portal_type=[
                'ps.plone.hosting.contact',
                'ps.plone.hosting.customer',
            ],
        ),
        title=_(u'Zone-C'),
    )


@implementer(IExternalDomain)
class ExternalDomain(Container):
    """`External Domain` content type."""


@implementer(IDomain)
class Domain(Container):
    """`Domain` content type."""
