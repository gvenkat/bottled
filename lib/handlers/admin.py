
from util.handler import Handler

class AdminHandler( Handler ):
  def get( self ):
    self.response.out.write( "Woohoo, this is the admin panel" )
