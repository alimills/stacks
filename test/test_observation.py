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

  def setup(self):
    self.testbed = testbed.Testbed()
    self.testbed.activate()
    self.testbed.init_datastore_v3_stub()

  def teardown(self):
    self.testbed.deactivate()

  def testCreate(self):
    observation = Observation()
    observation.station_id = 'abcd'
    observation.observed_at = datetime.datetime.now()
    observation.put()
