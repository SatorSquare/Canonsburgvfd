from uuid import uuid4

from google.appengine.ext import ndb
from google.appengine.ext import deferred
from google.appengine.api import users

from Infrastructure.Models import Models

import time

def getUpdate(id):
    if id:
        update = ndb.Key(urlsafe=id).get()
        if update:
            return update
    return Models.Update()
  
def upsertUpdate(key, account, title, text):
    update = getUpdate(key)
    update.author = account.nickname
    update.heading = time.strftime("%B, %Y")
    update.title = title
    update.text = text
    update.put()
    return update

def deleteUpdate(key):
    update = getUpdate(key)
    if update:
        if update.key:
            update.key.delete()
    
    
def getUpdates(prev_cursor_str, next_cursor_str, updatesPerPage):
    if not prev_cursor_str and not next_cursor_str:
        updates, next_cursor, more = Models.Update.query().order(-Models.Update.create_time).fetch_page(updatesPerPage)
        prev_cursor_str = ''
        if next_cursor:
            next_cursor_str = next_cursor.urlsafe()
        else:
            next_cursor_str = ''
        next_ = True if more else False
        prev = False
    elif next_cursor_str:
        cursor = Cursor(urlsafe=next_cursor_str)
        updates, next_cursor, more = Models.Update.query().order(-Models.Update.create_time).fetch_page(updatesPerPage, start_cursor=cursor)
        prev_cursor_str = next_cursor_str
        next_cursor_str = next_cursor.urlsafe()
        prev = True
        next_ = True if more else False
    elif prev_cursor_str:
        cursor = Cursor(urlsafe=prev_cursor_str)
        updates, next_cursor, more = Models.Update.query().order(Models.Update.create_time).fetch_page(photosPerPage, start_cursor=cursor)
        updates.reverse()
        next_cursor_str = prev_cursor_str
        prev_cursor_str = next_cursor.urlsafe()
        prev = True if more else False
        next_ = True
    return updates, next_cursor_str, prev_cursor_str, prev, next_