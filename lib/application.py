
from model import setting, user, content, entry, tag, tagmap
from google.appengine.ext.webapp import template
import os, os.path


class Application( object ):

  VERSION = '0.1'

  @classmethod
  def get_version( cls ):
    return float( cls.VERSION )

  @classmethod
  def has_been_setup( cls ):
    return setting.Setting.is_app_setup()

  # FIXME: Duplication
  @staticmethod
  def include( f, d ):

    _path = os.path.join(
      os.path.dirname( __file__ ),
      '..', 'themes', 'admin', f
    )

    print _path

    return template.render( _path, { } )

  @classmethod
  def themes( cls ):
    return setting.Setting.all_themes()


