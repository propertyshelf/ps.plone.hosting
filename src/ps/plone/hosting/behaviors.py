# -*- coding: utf-8 -*-
"""Miscellaneous behaviors for ps.plone.hosting content types."""

# zope imports
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from zope import schema
from zope.interface import alsoProvides

# local imports
from ps.plone.hosting import _


ADDRESS_FIELDS = (
    'street',
    'additional_address_details',
    'city',
    'region',
    'zip_code',
    'country',
)

CONTACT_DETAILS_FIELDS = (
    'lastname',
    'firstname',
    'company',
    'email',
    'phone',
    'cell_phone',
    'fax',
    'website',
)


class IContactDetails(model.Schema):
    """Contact details behavior."""

    fieldset(
        'contact_details',
        label=_(u'Contact Details'),
        fields=CONTACT_DETAILS_FIELDS,
    )
    fieldset(
        'address',
        label=_(u'Address'),
        fields=ADDRESS_FIELDS,
    )

    lastname = schema.TextLine(
        required=False,
        title=_(u'Lastname'),
    )

    firstname = schema.TextLine(
        required=False,
        title=_(u'Firstname'),
    )

    company = schema.TextLine(
        required=False,
        title=_(u'Company'),
    )

    email = schema.TextLine(
        required=False,
        title=_(u'Email'),
    )

    phone = schema.TextLine(
        required=False,
        title=_(u'Phone'),
    )

    cell_phone = schema.TextLine(
        required=False,
        title=_(u'Cell Phone'),
    )

    fax = schema.TextLine(
        required=False,
        title=_(u'Fax'),
    )

    website = schema.TextLine(
        required=False,
        title=_(u'Website'),
    )

    street = schema.TextLine(
        required=False,
        title=_(u'Street'),
    )

    additional_address_details = schema.TextLine(
        required=False,
        title=_(u'Additional address details'),
    )

    city = schema.TextLine(
        required=False,
        title=_(u'City/Town'),
    )

    region = schema.TextLine(
        required=False,
        title=_(u'Region'),
    )

    zip_code = schema.TextLine(
        required=False,
        title=_(u'ZIP'),
    )

    country = schema.TextLine(
        required=False,
        title=_(u'Country'),
    )

alsoProvides(IContactDetails, IFormFieldProvider)
