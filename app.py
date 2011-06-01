import os
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class Handler(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      url = users.create_logout_url("/")
      user_nickname = user.nickname()
      template_path = os.path.join(os.path.dirname(__file__), 'index.html')
    else:
      url = users.create_login_url("/")
      user_nickname = ""
      template_path = os.path.join(os.path.dirname(__file__), 'login.html')
    
    template_values = {
      'url': url,
      'user_nickname': user_nickname,
    }

    self.response.out.write(template.render(template_path, template_values))