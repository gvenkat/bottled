
import base
from model.setting import Setting

class Setup( base.Base ):

  def get( self ):
    self.render_template( 'setup.html', { } )



  def post( self ):

    req = self.request

    title = req.get( 'title' )
    theme = req.get( 'theme' )

    if not title or not theme:
      self.get()
      return

    Setting.save( {
      "title": title,
      "theme": theme
    } )

    if not Setting.is_app_setup():
      self.get()
      return
    else:
      self.redirect( '/admin/dashboard', { } )
      return











