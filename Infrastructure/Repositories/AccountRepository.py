from uuid import uuid4

from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from google.appengine.ext import deferred

from Infrastructure.Models import Models

def getAccount(key):
    return Models.AccountModel.get_by_id(key)
  
def createAccount(user):
    account = Models.AccountModel(id = user.user_id())
    account.email = user.email()
    account.nickname = user.nickname()
    account.put()
    return account
    