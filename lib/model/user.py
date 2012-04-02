from google.appengine.ext import db
from google.appengine.api import users



class User( db.Model ):
  user          = db.UserProperty()
  email         = db.EmailProperty()
  is_blog_owner = db.BooleanProperty()
