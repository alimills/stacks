from google.appengine.ext import db
from geo.geomodel import GeoModel
#from api.models.observation import Observation

class Station(GeoModel):
  station_id = db.StringProperty()
  created_at = db.DateTimeProperty(auto_now_add = True)
  updated_at = db.DateTimeProperty(auto_now = True)
  #most_recent_observation = db.ReferenceProperty(Observation)
