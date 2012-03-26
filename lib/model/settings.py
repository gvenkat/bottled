from google.appengine.ext import db
import datetime

class Settings( db.Model ):

  appname           = db.StringProperty()
  version           = db.StringProperty()
  theme             = db.StringProperty()
  created_at        = db.DateProperty()
  updated_at        = db.DateProperty()
  comments_enabled  = db.BooleanProperty()








