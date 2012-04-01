from google.appengine.ext import db
import entry, tag

class TagMap( db.Model ):
  entry   = db.ReferenceProperty( entry.Entry )
  tag     = db.ReferenceProperty( tag.Tag )


