#!/usr/bin/python2.4
#
# Copyright 2011 Google Inc. All Rights Reserved.

"""Tests for observation.

Found example here:
http://code.google.com/appengine/docs/python/tools/localunittesting.html

"""

__author__ = 'lbayes@google.com (Luke Bayes)'

import datetime
from test.stack_test_case import StackTestCase
from api.models.observation import Observation

class TestObservation(StackTestCase):

  def testCreateEmpty(self):
    instance = Observation().put()
    self.assertTrue(instance)

  def testCreateWithParam(self):
    instance = Observation(station_id = "abcd")
    self.assertEqual("abcd", instance.station_id)
