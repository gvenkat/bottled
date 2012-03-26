from google.appengine.ext import db
import tag.Tag, content.Content
import content

class TagMap( db.Model )
  tag     = db.ReferenceProperty( Tag )
  content = db.ReferenceProperty( Content )




