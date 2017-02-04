import os
import webapp2

from google.appengine.api import users
from google.appengine.ext import blobstore

from Configuration import Config

from Domain.Utilities import TemplateUtility

from Infrastructure.Repositories import AccountRepository

  
class MainHandler(webapp2.RequestHandler):    
    def get(self):
        account = None;
        user = users.get_current_user()
        if user:
            account = AccountRepository.getAccount(user.user_id())
            if not account:
                account = AccountRepository.createAccount(user, users.is_current_user_admin())
                
        # Inserts the templates for the linked pages
        template_values = {
            'BODY' : TemplateUtility.render(Config.ROUTE_MAP.get(self.request.path, Config.ROUTE_MAP['/']), { 'ACCOUNT': account }),
            'PATH' : self.request.path,
            'URL' : self.request.url,
            'LOGIN_URL': users.create_login_url('/'),
            'LOGOUT_URL': users.create_logout_url('/'),
            'ACCOUNT': account,
            'PHOTO_UPLOAD_URL': blobstore.create_upload_url('/UploadPhoto')
        }
  
        self.response.write(TemplateUtility.render('index.html', template_values))
      