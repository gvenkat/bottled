
from google.appengine.ext import webapp

class Handler( webapp.RequestHandler ):

  def parts( self ):
    return self.request.path.split( '/' )[1:]
