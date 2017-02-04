from google.appengine.ext import ndb
from google.appengine.ext import blobstore

from Infrastructure.Models import Models
  
def uploadPhoto(upload):
    photo = Models.Photo( full_size_image_key = upload.key() )
    photo.put()
    return photo