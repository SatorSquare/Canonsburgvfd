from google.appengine.ext import ndb
  
class AccountModel(ndb.Model):
  create_time = ndb.DateTimeProperty(auto_now_add = True)
  mod_time = ndb.DateTimeProperty(auto_now = True)
  email = ndb.StringProperty(required = True)
  nickname = ndb.StringProperty(required = True)