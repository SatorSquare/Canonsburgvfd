from uuid import uuid4

from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from google.appengine.ext import deferred
from google.appengine.api import users

from Infrastructure.Models import Models

def getAccount(key):
    return Models.AccountModel.get_by_id(key)
  
def createAccount(user, isAdmin):
    account = Models.AccountModel(id = user.user_id())
    account.email = user.email()
    account.nickname = user.nickname()
    account.admin = 1 if isAdmin else 0
    account.put()
    return account
    
def getUserAccount():
    account = None;
    user = users.get_current_user()
    if user:
        account = getAccount(user.user_id())
        if not account:
            account = createAccount(user, users.is_current_user_admin())
    return account
