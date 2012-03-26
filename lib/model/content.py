from google.appengine.ext import db
from google.appengine.api import users

import datetime

class Content( db.Model ):

  title       = db.StringProperty()
  created_at  = db.DateTimeProperty()
  created_by  = users.User()
  content     = db.StringProperty()

