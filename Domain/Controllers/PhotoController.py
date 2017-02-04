from Domain.Utilities import ImageUtility
from Infrastructure.Models import Models
from Infrastructure.Repositories import PhotoRepository

from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

import webapp2

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
            if blob_info:
                image = ImageUtility.adjustContrast(blob_key)

                self.response.headers['Content-Type'] = 'image/jpeg'
                self.response.out.write(image)
                return

        # Either "id" wasn't provided, or there was no image with that ID
        # in the datastore.
        self.error(404)
        
class PhotoUploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        upload = self.get_uploads()[0]
        result = PhotoRepository.uploadPhoto(upload);
        self.response.out.write(result.full_size_image_key)