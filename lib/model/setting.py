from google.appengine.ext import db

class Setting( db.Model ):
  app_name            = db.StringProperty( required=True )
  app_version         = db.FloatProperty( required=True )
  app_theme           = db.StringProperty()
  allow_registration  = db.BooleanProperty()

  _cache = None

  @classmethod
  def _fill_cache( cls ):

    # Get only the first entry
    # This model should never have more
    # one entry
    if _cache is None:
      _cache = cls.get()

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

    if _cache is not None:
      _cache.__get__( prop )






