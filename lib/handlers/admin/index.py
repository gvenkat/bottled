
from util.handler import Handler
import base


class AdminHandler( base.Base ):

  def get( self ):
    self.response.out.write( "Woohoo! This is the admin panel" )
