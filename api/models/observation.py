from google.appengine.ext import db
from geo.geomodel import GeoModel
from api.models.station import Station

class Observation(GeoModel):
  station = db.ReferenceProperty(Station)
  created_at = db.DateTimeProperty(auto_now_add = True)
  observed_at = db.DateTimeProperty()
