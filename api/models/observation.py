from google.appengine.ext import db
from geo.geomodel import GeoModel

class Observation(GeoModel):
  station_id = db.StringProperty( required = True )
  created_at = db.DateTimeProperty(auto_now_add = True)
  observed_at = db.DateTimeProperty()
  wave_height_meters = db.FloatProperty()
