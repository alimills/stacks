from google.appengine.ext import db
from geo.geomodel import GeoModel

class Observation(GeoModel):
  station_id = db.StringProperty()
  created_at = db.DateTimeProperty(auto_now_add = True)
  observed_at = db.DateTimeProperty()
