
from util.handler import Handler

class AdminHandler( Handler ):
  def get( self ):
    self.response.out.write( "Woohoo! This is the admin panel" )
