from google.appengine.ext import db
import user

class Content( db.polymodel.PolyModel ):
  created_by       = db.ReferenceProperty( user.User )
  created_at       = db.DateTimeProperty()
  updated_at       = db.DateTimeProperty()


