
from util.handler import Handler
import base, application, sys
from datetime import datetime
from google.appengine.api import users
from model.entry import Entry


class AdminHandler( base.Base ):

  def get( self ):

    allowed = [
      'dashboard',
      'settings',
      'new',
      'edit',
      'all'
    ]

    if len( self.parts() ) < 2 or not self.parts()[1]:
      self.dashboard()
    elif self.parts()[1] in allowed:
      self.__getattribute__( self.parts()[1] )()
    else:
      # self.not_found()
      pass

  # Dispatch posts to get too
  # that dispatches it to other places anyway
  def post( self ):
    # Flag POST requests
    self.method = 'POST'
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
    _p = self._default_params()

    _p.update( {
      "items": Entry.all().fetch( Entry.all().count() ),
      "user": users.get_current_user()
    } )

    self.render_template( 'all.html', _p )


  def edit( self ):

    _entry = None

    try:
      _key = self.request.get( '_post' )

      _entry = Entry.get_by_key_name( _key )

      print _entry

    except:
      print sys.exc_info()

    print _entry
    self.render_template( 'new.html', { 'entry': _entry } )



  def settings( self ):
    self.render_template( 'settings.html', self._default_params() )

  def new( self ):

    req = self.request

    try:
      if 'POST' in self.method:
        _title  = req.get( 'title' )
        _entry  = req.get( 'entry' )
        _updated = _now = datetime.now()
        _created_by = users.get_current_user()

        Entry(
          title       = _title,
          content     = _entry,
          created_at  = _now,
          updated_at  = _now,
          created_by  = _created_by
        ).put()

    except:
      # print sys.exc_info()
      pass
    finally:
      self.render_template( 'new.html', self._default_params() )


