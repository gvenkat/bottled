from google.appengine.ext import db


class User( db.Model ):
  user          = db.UserProperty()
  email         = db.EmailProperty()
  is_blog_owner = db.BooleanProperty()
