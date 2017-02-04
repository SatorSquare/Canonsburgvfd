import os
import webapp2

from google.appengine.api import users
from google.appengine.ext import blobstore

from Configuration import Config

from Domain.Utilities import TemplateUtility

from Infrastructure.Repositories import AccountRepository


class StaticHandler(webapp2.RequestHandler):    
  def get(self):
      account = None;
      user = users.get_current_user()
      if user:
        account = AccountRepository.getAccount(user.user_id())
        if not account:
            account = AccountRepository.createAccount(user, users.is_current_user_admin())
                
      # Inserts the templates for the linked pages
      template_values = {
        'PATH' : self.request.path,
        'URL' : self.request.url,
        'ACCOUNT' : account
      }
      
      path = self.request.path.replace("/Static", "")
      self.response.write(TemplateUtility.render(Config.ROUTE_MAP.get(path, Config.ROUTE_MAP['/']), template_values))