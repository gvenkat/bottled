
from util.handler import Handler
import base, application


class AdminHandler( base.Base ):

  def get( self ):
    allowed = [
      'dashboard',
      'settings',
      'new',
      'all'
    ]

    if self.parts()[1] in allowed:
      self.__getattribute__( self.parts()[1] )()
    else:
      # FIXME: To be implemented
      # self.not_found()
      pass

  # Dispatch posts to get too
  # that dispatches it to other places anyway
  def post( self ):
    self.get()

  def _default_params( self ):
    return {
      "show_top_bar": True,
      "include": application.Application.include
    }

  # FIXME: Stub implementations
  def dashboard( self ):
    self.render_template( 'dashboard.html', self._default_params() )

  def all( self ):
    self.render_template( 'all.html', self._default_params() )

  def settings( self ):
    self.render_template( 'settings.html', self._default_params() )

  def new( self ):
    self.render_template( 'new.html', self._default_params() )


