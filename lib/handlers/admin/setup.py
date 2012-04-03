
import base

class Setup( base.Base ):

  def get( self ):
    self.render_template( 'setup.html', { } )


