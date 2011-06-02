import datetime

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import urlfetch
from api.models.observation import Observation
from api.lib.noaa_latest_observation_parser import NoaaLatestObservationParser

class Handler(webapp.RequestHandler):
  observation_url = "http://www.ndbc.noaa.gov/data/latest_obs/latest_obs.txt"

  def get(self):
    response = urlfetch.fetch(self.observation_url)
    if response.status_code == 200 :
      parser = NoaaLatestObservationParser()
      records = parser.parse(response.content)
      for record in records:
        self.store_record(record)
    else :
      print "FAILED TO LOAD from %s with: %s", observation_url, response.status_code

  def store_record(self, record):
    station_id = record.get('station_id')
    wave_height = record.get('wave_height_meters')

    if wave_height is not None :
      observation = Observation(
        station_id = station_id,
        wave_height_meters = float(wave_height),
      )
      observation.put()
