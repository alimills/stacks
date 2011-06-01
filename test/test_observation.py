#!/usr/bin/python2.4
#
# Copyright 2011 Google Inc. All Rights Reserved.

"""Tests for observation.

Found example here:
http://code.google.com/appengine/docs/python/tools/localunittesting.html

"""

__author__ = 'lbayes@google.com (Luke Bayes)'

#from google3.testing.pybase import googletest
import unittest
import datetime
from google.appengine.ext import db
from google.appengine.ext import testbed
from api.models.observation import Observation

class TestObservation(unittest.TestCase):

  def setUp(self):
    self.testbed = testbed.Testbed()
    self.testbed.setup_env(app_id = "12345")
    self.testbed.activate()
    self.testbed.init_datastore_v3_stub()

  def tearDown(self):
    self.testbed.deactivate()

  def testCreateEmpty(self):
    instance = Observation().put()
    self.assertTrue(instance)

  def testCreateWithParam(self):
    instance = Observation(station_id = "abcd")
    self.assertEqual("abcd", instance.station_id)
