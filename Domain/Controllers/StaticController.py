import os
import webapp2

from google.appengine.api import users

from Configuration import Config

from Domain.Utilities import TemplateUtility

class StaticHandler(webapp2.RequestHandler):    
  def get(self):
      # Inserts the templates for the linked pages
      template_values = {
        'PATH' : self.request.path,
        'URL' : self.request.url
      }
      path = self.request.path.replace("/Static", "")
      self.response.write(TemplateUtility.render(Config.ROUTE_MAP.get(path, Config.ROUTE_MAP['/']), template_values))