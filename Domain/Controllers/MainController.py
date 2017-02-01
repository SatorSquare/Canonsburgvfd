import os
import webapp2

from google.appengine.api import users

from Configuration import Config

from Domain.Utilities import TemplateUtility

  
class MainHandler(webapp2.RequestHandler):    
  def get(self):        
      # Inserts the templates for the linked pages
      template_values = {
        'BODY' : TemplateUtility.render(Config.ROUTE_MAP.get(self.request.path, Config.ROUTE_MAP['/']), {}),
        'PATH' : self.request.path,
        'URL' : self.request.url,
      }
      
      self.response.write(TemplateUtility.render('index.html', template_values))