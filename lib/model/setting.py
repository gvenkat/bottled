from google.appengine.ext import db
import os, os.path
import application


class Setting( db.Model ):
  app_name            = db.StringProperty( required=True )
  app_version         = db.FloatProperty( required=True )
  app_theme           = db.StringProperty()
  allow_registration  = db.BooleanProperty()

  _cache = None

  @classmethod
  def save( cls, d ):
    _s = Setting(
      app_name = d[ 'title' ],
      app_version = application.Application.get_version(),
      app_theme = d[ 'theme' ],
      allow_registraion = False
    )

    _s.put()


  @classmethod
  def _fill_cache( cls, force=False ):

    # Get only the first entry
    # This model should never have more
    # one entry
    if cls._cache is None or force is True:
      cls._cache = cls.all().get()

  @classmethod
  def all_themes( cls ):

    _path = os.path.join(
      os.path.dirname( __file__ ),
      '..', '..', 'themes'
    )

    return [ i for i in os.listdir( _path ) if i != 'admin' ]


  # FIXME: Maybe there's a better way to write these
  # Accessors
  @classmethod
  def name( cls ):
    return cls._get_property( 'app_name' )

  @classmethod
  def version( cls ):
    return "%.2f" % ( cls._get_property( 'app_version' ) )

  @classmethod
  def _get_property( cls, prop ):
    cls._fill_cache()

    if cls._cache is not None:
      return cls._cache.__dict__[ '_' + prop ]


  @classmethod
  def is_app_setup( cls ):
    cls._fill_cache( True )

    return cls._cache is not None



