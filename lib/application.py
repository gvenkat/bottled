
from model import setting, user, content, entry, tag, tagmap


class Application( object ):

  VERSION = '0.1'

  @classmethod
  def get_version( cls ):
    return float( cls.VERSION )

  @classmethod
  def has_been_setup( cls ):
    return setting.Setting.is_app_setup()

  @classmethod
  def themes( cls ):
    return setting.Setting.all_themes()
