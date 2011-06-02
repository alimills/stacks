import datetime

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from protorpc import message_types
from protorpc import messages
from protorpc import remote

class ObservationRequest(messages.Message):
 	id = messages.StringField(1)
	lat = messages.IntegerField(2)
	lng = messages.IntegerField(3)
	limit = messages.IntegerField(4, default=10)

class ObservationResponse(messages.Message):
#	observed_at = messages.IntegerField(1)
	lat = messages.IntegerField(2)
	lng = messages.IntegerField(3)

class ObservationsResponse(messages.Message):
  observations = messages.MessageField(ObservationResponse, 1, repeated=True)

class Service(remote.Service):

  @remote.method(ObservationRequest, message_types.VoidMessage)
  def create(self, request):
		return message_types.VoidMessage()

  @remote.method(ObservationRequest, ObservationResponse)
  def by_id(self, request):
    return self.create_observation()

  @remote.method(ObservationRequest, ObservationsResponse)
  def by_lat_lng(self, request):
    return self.create_observation()

  @remote.method(ObservationRequest, ObservationsResponse)
  def all(self, request):
		return ObservationsResponse(observations=[self.create_observation(),self.create_observation()])

  def create_observation(self):
		observed_at = datetime.datetime.now()
		lat = 123
		lng = 456
		return ObservationResponse(lat=lat,lng=lng)