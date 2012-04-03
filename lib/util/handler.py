
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users

import os, os.path

import application



class Handler( webapp.RequestHandler ):

  theme = 'default'

  def get_template_dir( self ):
    return os.path.join(
      os.path.dirname( __file__ ),
      '..', '..', 'themes', self.get_theme()
    )

  def get_wrapper_path( self ):
    return os.path.join(
      self.get_template_dir(),
      'wrapper.html'
    )

  def wrapper_exists( self ):

    return os.path.exists(
      self.get_wrapper_path()
    )

  def to_path( self, template ):
    return os.path.join(
      self.get_template_dir(),
      template
    )

  def _user( self ):
    return users.get_current_user()

  def _render( self, t, d ):

    _d = {
      "user": self._user(),
      "is_user_logged_in": ( self._user() is not None ),
      "login_url": users.create_login_url(),
      "application": application.Application
    }

    d.update( _d )

    _rendered = template.render(
      self.to_path( t ),
      d
    )

    _wrendered = None

    if self.wrapper_exists():

      d.update(
        {
          "content": _rendered
        }
      )

      _wrendered = template.render(
        self.to_path( 'wrapper.html' ),
        d
      )

    if _wrendered is None:
      return _rendered
    else:
      return _wrendered



  def render_template( self, t, d, publish=True ):

    _html = self._render( t, d )

    if publish is True:
      self.response.out.write( _html )
    else:
      return _html


    return True


  def parts( self ):
    return self.request.path.split( '/' )[1:]


  def set_theme( self, theme ):
    Handler.theme = theme


  def get_theme( self ):
    return Handler.theme

