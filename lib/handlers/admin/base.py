
from util.handler import Handler

class Base( Handler ):

  # FIXME: Hardcoded, must use class variable??
  def get_theme( self ):
    return 'admin'

  def __initialize__( self, *args, **kwargs ):
    self.set_theme( 'admin' )
    super( self, *args, **kwargs )

