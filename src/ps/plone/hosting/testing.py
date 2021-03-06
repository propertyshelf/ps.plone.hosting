# -*- coding: utf-8 -*-
"""Test Layer for ps.plone.hosting."""

# zope imports
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
    PLONE_FIXTURE,
)
from plone.testing import Layer, z2
from zope.configuration import xmlconfig


class Fixture(PloneSandboxLayer):
    """Custom Test Layer for ps.plone.hosting."""
    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        """Set up Zope for testing."""
        # Load ZCML
        import ps.plone.hosting
        xmlconfig.file(
            'configure.zcml',
            ps.plone.hosting,
            context=configurationContext,
        )

    def setUpPloneSite(self, portal):
        """Set up a Plone site for testing."""
        self.applyProfile(portal, 'ps.plone.hosting:default')


FIXTURE = Fixture()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE, ),
    name='ps.plone.hosting:Integration',
)

FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE, z2.ZSERVER_FIXTURE),
    name='ps.plone.hosting:Functional',
)

ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(FIXTURE, REMOTE_LIBRARY_BUNDLE_FIXTURE, z2.ZSERVER_FIXTURE),
    name='ps.plone.hosting:Acceptance')

ROBOT_TESTING = Layer(name='ps.plone.hosting:Robot')
