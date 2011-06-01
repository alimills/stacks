#!/usr/bin/python2.4
#
# Copyright 2011 Google Inc. All Rights Reserved.

"""The base class for all geospatial, natural observations.

Some example observations can be found here:

http://www.ndbc.noaa.gov/data/latest_obs/latest_obs.txt
"""

__author__ = 'lbayes@google.com (Luke Bayes)'

from google.appengine.ext import db

class Observation(db.Model):
  lat = db.StringProperty()
  lng = db.StringProperty()
  station_id = db.StringProperty()
