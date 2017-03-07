import webapp2

from webapp2_extras import json

from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

from Configuration import Config
from Infrastructure.Models import Models
from Domain.Utilities import TemplateUtility
from Infrastructure.Repositories import UpdateRepository
from Infrastructure.Repositories import AccountRepository

class DeleteUpdateHandler(webapp2.RequestHandler):
    def post(self):
        id = self.request.get("id")
        UpdateRepository.deleteUpdate(id)
        self.response.out.write(json.encode({}))
    
class UpdateHandler(webapp2.RequestHandler):
    def post(self):
        account = AccountRepository.getUserAccount();
        if account.admin == 0:
            return false
            
        id = self.request.get("id")
        title = self.request.get("title")
        text = self.request.get("text")
        
        UpdateRepository.upsertUpdate(id, account, title, text)
        self.response.out.write(json.encode({}))
    
    """Handles requests like /PhotoGallery?page=1234567."""   
    def get(self):
        account = AccountRepository.getUserAccount()
        updates, next_cursor_str, prev_cursor_str, prev, next = UpdateRepository.getUpdates(self.request.get('prev_cursor', ''), self.request.get('next_cursor', ''), Config.UPDATES_PER_PAGE)
            
        # Inserts the templates for the linked pages
        template_values = {
            'ACCOUNT' : account,
            'UPDATES' : updates,
            'NEXT_CURSOR' : next_cursor_str,
            'PREV_CURSOR' : prev_cursor_str,
            'PREV' : prev,
            'NEXT' : next
        }

        self.response.write(TemplateUtility.render(Config.ROUTE_MAP.get('/Updates', Config.ROUTE_MAP['/']), template_values))