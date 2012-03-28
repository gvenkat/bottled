from google.appengine.ext import db


class Tag( db.Model ):

  tag = db.StringProperty( required=True )


  @classmethod
  def count( cls ):
    return cls.all().count()

  @classmethod
  def all_tags( cls ):
    return [ i.tag for i in cls.all().fetch( cls.count() ) ]




