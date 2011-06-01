from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from protorpc import messages
from protorpc import remote

class Request(messages.Message):
  my_name = messages.StringField(1, required=True)

class Response(messages.Message):
  hello = messages.StringField(1, required=True)

class Service(remote.Service):

  @remote.method(Request, Response)
  def hello(self, request):
    return Response(hello='Hello there, %s!' % request.my_name)