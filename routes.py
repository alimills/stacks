import app, os, sys

sys.path.insert(0, 'vendor')
sys.path.insert(0, 'api/lib')

from api.controllers import observations

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from protorpc import service_handlers

def main():

  application = webapp.WSGIApplication(
    service_handlers.service_mapping([
  	  ('/api/observations', observations.Service),
  	]) + 
  	[('/', app.Handler)],debug=True)

  run_wsgi_app(application)

if __name__ == "__main__":
  main()
