from google.appengine.ext import db
import content

class Entry( content.Content ):
  title   = db.StringProperty()
  content = db.TextProperty()

