from google.appengine.ext import db
from google.appengine.ext.db import polymodel
import user

class Content( polymodel.PolyModel ):
  created_by       = db.UserProperty()
  created_at       = db.DateTimeProperty()
  updated_at       = db.DateTimeProperty()


