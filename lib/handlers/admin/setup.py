from util.handler import Handler

class Setup( Handler ):

  def get( self ):
    self.response.out.write( "ABout to set things up" )
