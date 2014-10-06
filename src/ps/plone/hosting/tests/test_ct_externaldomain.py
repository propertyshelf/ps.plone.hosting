# -*- coding: utf-8 -*-
"""Test 'External Domain' Content Type."""

# python imports
import unittest2 as unittest

# zope imports
from Products.CMFCore.utils import getToolByName
from plone import api
from plone.app.content.interfaces import INameFromTitle
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject, queryUtility

# local imports
from ps.plone.hosting.content.domain import IExternalDomain
from ps.plone.hosting.testing import INTEGRATION_TESTING


CT = 'ps.plone.hosting.externaldomain'


class ExternalDomainIntegrationTestCase(unittest.TestCase):
    """Test Case for the 'ps.plone.hosting.externaldomain' content type."""
    layer = INTEGRATION_TESTING

    def setUp(self):
        """Additional test setup."""
        self.portal = self.layer['portal']

        with api.env.adopt_roles(['Manager']):
            self.directory = api.content.create(
                self.portal, 'ps.plone.hosting.directory', 'directory',
            )
            self.customer = api.content.create(
                self.directory, 'ps.plone.hosting.customer', 'customer',
            )

        self.ct = api.content.create(self.customer, CT, 'ct1')

    def test_ct_available(self):
        """Validate that the content type is available."""
        portal_types = getToolByName(self.portal, 'portal_types')
        self.assertTrue(CT in portal_types)

    def test_fti(self):
        """Validate that the factory type information is available."""
        fti = queryUtility(IDexterityFTI, name=CT)
        self.assertIsNotNone(fti)

    def test_adding(self):
        """Validate the created content type."""
        self.assertTrue(IExternalDomain.providedBy(self.ct))

    def test_schema(self):
        """Validate the correct schema."""
        fti = queryUtility(IDexterityFTI, name=CT)
        schema = fti.lookupSchema()
        self.assertEqual(IExternalDomain, schema)

    def test_factory(self):
        """Validate the content type factory."""
        fti = queryUtility(IDexterityFTI, name=CT)
        factory = fti.factory
        new_object = createObject(factory)
        self.assertTrue(IExternalDomain.providedBy(new_object))

    def test_behaviors(self):
        """Validate that the required behaviors are available."""
        self.assertTrue(INameFromTitle.providedBy(self.ct))
