from google.appengine.ext import db
import model.content


class ContentChildren( db.Model ):
  parent = db.ReferenceProperty( content.Content )
  child  = db.RerenceProperty( content.Content )


