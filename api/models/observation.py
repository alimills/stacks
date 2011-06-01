#!/usr/bin/python2.4
#
# Copyright 2011 Google Inc. All Rights Reserved.

"""The base class for all geospatial, natural observations.

Some example observations can be found here:

http://www.ndbc.noaa.gov/data/latest_obs/latest_obs.txt
"""

__author__ = 'lbayes@google.com (Luke Bayes)'

from google.appengine.ext import db
from api.lib.geomodel import GeoModel

class Observation(GeoModel)
  station_id = db.StringProperty()
  created_at = db.DateTimeProperty(auto_now_add = True)
  observed_at = db.DateTimeProperty()
