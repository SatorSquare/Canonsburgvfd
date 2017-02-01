from Domain.Utilities import ImageUtility
from Infrastructure.Models import Models

import webapp2

class ThumbnailHandler(webapp2.RequestHandler):
    def get(self):
        if self.request.get("id"):
            photo = Models.Photo.get_by_id(int(self.request.get("id")))

            if photo:
                thumbnail = ImageUtility.thumbnailify(photo.full_size_image)

                self.response.headers['Content-Type'] = 'image/jpeg'
                self.response.out.write(thumbnail)
                return

        # Either "id" wasn't provided, or there was no image with that ID
        # in the datastore.
        self.error(404)
        
class PhotoHandler(webapp2.RequestHandler):
    def get(self):
        if self.request.get("id"):
            photo = Models.Photo.get_by_id(int(self.request.get("id")))

            if photo:
                image = ImageUtility.adjustContrast(photo.full_size_image)

                self.response.headers['Content-Type'] = 'image/jpeg'
                self.response.out.write(image)
                return

        # Either "id" wasn't provided, or there was no image with that ID
        # in the datastore.
        self.error(404)