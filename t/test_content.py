
import sys,unittest
from os.path import dirname
from google.appengine.api import users

sys.path.append( dirname( __file__ ) + '/../lib' )

from util import apptest
from model import content
from datetime import datetime

class ContentTestCase( apptest.BottledTestCase ):

  def _create_content( self ):
    self.setup_user()

    _c = content.Content(
      created_by = users.get_current_user(),
      created_at = datetime.now(),
      updated_at = datetime.now()
    )

    _c.put()
    self.isNotNone( _c )
    return _c


  def testCreate( self ):
    self._create_content()


  def testListCreated( self ):
    now = datetime.now()
    _c = self._create_content()

    item = content.Content.all().get()
    self.assertEquals( content.Content.all().count(), 1 )
    self.assertEquals(  item.created_by, users.get_current_user() )

  def testDestroyCreated( self ):
    _c = self._create_content()
    item = content.Content.all().get()

    self.assertEquals( content.Content.all().count(), 1 )
    self.assertEquals(  item.created_by, users.get_current_user() )

    content.Content.all().get().delete()

    self.assertEquals( content.Content.all().count(), 0 )




