from google.appengine.ext import db
import datetime
import model.content.Content
import util.validators

class Comments( db.PolyModel ):
  created_at  = db.DateTimeProperty()
  user        = db.UserProperty()
  content     = db.ReferenceProperty( Content )
  ip_address  = db.StringProperty( required=True, validator = util.validators.validate_ip )
  comment     = db.TextProperty( required = True )




