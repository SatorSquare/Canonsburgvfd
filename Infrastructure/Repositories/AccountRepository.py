from uuid import uuid4

from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from google.appengine.ext import deferred

from Models import AccountModel

class AccountBroker:
  @staticmethod
  def getAccount(key):
    return AccountModel.get_by_id(key)
  
  @staticmethod
  def createAccount(user):
    account = AccountModel(id = user.user_id())
    account.email = user.email()
    account.nickname = user.nickname()
    account.put()
    return account
    