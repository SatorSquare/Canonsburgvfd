import webapp2
from webapp2_extras import json

from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

from Configuration import Config
from Infrastructure.Models import Models
from Domain.Utilities import ImageUtility
from Domain.Utilities import TemplateUtility
from Infrastructure.Repositories import PhotoRepository
from Infrastructure.Repositories import AccountRepository

class ThumbnailHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, blob_key):
        if blob_key:
            blob_info = blobstore.get(blob_key)
            if blob_info:
                thumbnail = ImageUtility.thumbnailify(blob_key)

                self.response.headers['Content-Type'] = 'image/jpeg'
                self.response.out.write(thumbnail)
                return

        # Either "id" wasn't provided, or there was no image with that ID
        # in the datastore.
        self.error(404)
        
class PhotoHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, blob_key):
        if blob_key:
            blob_info = blobstore.get(blob_key)
            if blobstore.get(blob_key):
                self.send_blob(blob_key)
                return

        # Either "id" wasn't provided, or there was no image with that ID
        # in the datastore.
        self.error(404)
        
class PhotoUploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        upload = self.get_uploads()[0]
        fileInfo = self.get_file_infos()[0]
        result = PhotoRepository.uploadPhoto(upload, fileInfo)
        self.response.out.write(json.encode({}));
        
class PhotoGalleryHandler(webapp2.RequestHandler):
    """Handles requests like /PhotoGallery?page=1234567."""   
    def get(self):
        account = AccountRepository.getUserAccount()
        photos, next_cursor_str, prev_cursor_str, prev, next = PhotoRepository.getPhotos(self.request.get('prev_cursor', ''), self.request.get('next_cursor', ''), Config.GALLERY_PHOTOS_PER_PAGE)

        
        # Inserts the templates for the linked pages
        template_values = {
            'ACCOUNT' : account,
            'PHOTOS' : photos,
            'NEXT_CURSOR' : next_cursor_str,
            'PREV_CURSOR' : prev_cursor_str,
            'PREV' : prev,
            'NEXT' : next
        }
  
        self.response.write(TemplateUtility.render(Config.ROUTE_MAP.get('/PhotoGallery2', Config.ROUTE_MAP['/']), template_values))