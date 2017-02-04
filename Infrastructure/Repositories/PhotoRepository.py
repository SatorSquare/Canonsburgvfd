import os
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from google.appengine.datastore.datastore_query import Cursor

from Infrastructure.Models import Models
  
def uploadPhoto(upload, fileInfo):
    photo = Models.Photo( 
        full_size_image_key = upload.key(),
        title = os.path.splitext(fileInfo.filename)[0],
        filename = fileInfo.filename,
        content_type = fileInfo.content_type,
        creation = fileInfo.creation,
        size = fileInfo.size,
        md5_hash = fileInfo.md5_hash,
        gs_object_name = fileInfo.gs_object_name
    )
    photo.put()
    return photo
    
def getPhotos2(page, reverse, greetingsPerPage):
    q = Models.Photo.query()
    q_forward = q.order(-Models.Photo.mod_time)
    q_reverse = q.order(Models.Photo.mod_time)
    
    initial_cursor = Cursor(urlsafe=page)
    
    # Fetch a page going forward.
    photos, cursor, more = q_forward.fetch_page(greetingsPerPage, start_cursor=initial_cursor)
    
    # Fetch the same page going backward.
    r_photos, r_cursor, r_more = q_reverse.fetch_page(greetingsPerPage, start_cursor=initial_cursor)
    
    return photos, cursor, more, r_photos, r_cursor, r_more
    
def getPhotos(prev_cursor_str, next_cursor_str, greetingsPerPage):
    if not prev_cursor_str and not next_cursor_str:
        photos, next_cursor, more = Models.Photo.query().order(-Models.Photo.mod_time).fetch_page(greetingsPerPage)
        prev_cursor_str = ''
        if next_cursor:
            next_cursor_str = next_cursor.urlsafe()
        else:
            next_cursor_str = ''
        next_ = True if more else False
        prev = False
    elif next_cursor_str:
        cursor = Cursor(urlsafe=next_cursor_str)
        photos, next_cursor, more = Models.Photo.query().order(-Models.Photo.mod_time).fetch_page(greetingsPerPage, start_cursor=cursor)
        prev_cursor_str = next_cursor_str
        next_cursor_str = next_cursor.urlsafe()
        prev = True
        next_ = True if more else False
    elif prev_cursor_str:
        cursor = Cursor(urlsafe=prev_cursor_str)
        photos, next_cursor, more = Models.Photo.query().order(Models.Photo.mod_time).fetch_page(greetingsPerPage, start_cursor=cursor)
        photos.reverse()
        next_cursor_str = prev_cursor_str
        prev_cursor_str = next_cursor.urlsafe()
        prev = True if more else False
        next_ = True
    return photos, next_cursor_str, prev_cursor_str, prev, next_