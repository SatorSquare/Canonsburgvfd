import webapp2

from Domain.Controllers import MainController
from Domain.Controllers import StaticController
from Domain.Controllers import PhotoController

app = webapp2.WSGIApplication([
    ('/', MainController.MainHandler),
    ('/FirePrevention', MainController.MainHandler),
    ('/JoinUs', MainController.MainHandler),
    ('/Personnel', MainController.MainHandler),
    ('/Apparatus', MainController.MainHandler),
    ('/History', MainController.MainHandler),
    ('/Community', MainController.MainHandler),
    ('/PhotoGallery', MainController.MainHandler),
    ('/ContactUs', MainController.MainHandler),
    ('/Static/', StaticController.StaticHandler),
    ('/Static/FirePrevention', StaticController.StaticHandler),
    ('/Static/JoinUs', StaticController.StaticHandler),
    ('/Static/Personnel', StaticController.StaticHandler),
    ('/Static/Apparatus', StaticController.StaticHandler),
    ('/Static/History', StaticController.StaticHandler),
    ('/Static/Community', StaticController.StaticHandler),
    ('/Static/PhotoGallery', PhotoController.PhotoGalleryHandler),
    ('/Static/ContactUs', StaticController.StaticHandler),
    ('/Thumbnail/([^/]+)?', PhotoController.ThumbnailHandler),
    ('/Photo/([^/]+)?', PhotoController.PhotoHandler),
    ('/UploadPhoto', PhotoController.PhotoUploadHandler)
  ], debug=False)