from google.appengine.ext import db
import datetime


class Tag( db.Model ):

  tag         = db.StringProperty()
  created_at  = db.DateProperty()
  active      = db.BooleanProperty()


  def is_active( self ):
    return self.active

