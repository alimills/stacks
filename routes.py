import app
from api.controllers import stubs

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

def main():
  application = webapp.WSGIApplication([
    ('/', app.Handler),
    ('/api/stubs/', stubs.Handler)
  ],debug=True)

  run_wsgi_app(application)

if __name__ == "__main__":
  main()