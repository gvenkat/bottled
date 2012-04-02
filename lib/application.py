
from model import setting, user, content, entry, tag, tagmap


class Application( object ):

  @classmethod
  def has_been_setup( cls ):
    return setting.Setting.is_app_setup()


