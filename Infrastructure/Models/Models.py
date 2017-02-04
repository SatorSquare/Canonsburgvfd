from google.appengine.ext import ndb
  
class AccountModel(ndb.Model):
    create_time = ndb.DateTimeProperty(auto_now_add = True)
    mod_time = ndb.DateTimeProperty(auto_now = True)
    email = ndb.StringProperty(required = True)
    nickname = ndb.StringProperty(required = True)
    admin = ndb.IntegerProperty(default = 0)
    avatar = ndb.BlobProperty()

class Photo(ndb.Model):
    create_time = ndb.DateTimeProperty(auto_now_add = True)
    mod_time = ndb.DateTimeProperty(auto_now = True)
    full_size_image_key = ndb.BlobKeyProperty()
    title = ndb.StringProperty()
    filename = ndb.StringProperty()
    content_type = ndb.StringProperty()
    creation = ndb.DateTimeProperty()
    size = ndb.IntegerProperty()
    md5_hash = ndb.StringProperty()
    gs_object_name = ndb.StringProperty()