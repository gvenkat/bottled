
import sys,unittest
from os.path import dirname

sys.path.append( dirname( __file__ ) + '/../lib' )

from util import apptest
from model import entry
from datetime import datetime
from google.appengine.api import users

class EntryTestCase( apptest.BottledTestCase ):

  def _create_entry( self ):
    self.setup_user()
    now = datetime.now()

    _e = entry.Entry(
      created_by  = users.get_current_user(),
      created_at  = now,
      updated_at  = now,
      title       = "Foo",
      content     = "Bar"
    )

    _e.put()

    return _e

  def _create_entries( self, num ):

    for i in xrange( 0, num ):
      self._create_entry()

    return True



  def testCreate( self ):
    _e = self._create_entry()

    self.isNotNone( _e )
    self.assertEquals( _e.title, "Foo" )
    self.assertEquals( _e.content, "Bar" )
    self.assertEquals( _e.created_by, users.get_current_user() )


  def testList( self ):
    self._create_entries( 10 )
    self.assertEquals( entry.Entry.all().count(), 10 )

    results = entry.Entry.all().fetch( 10 )

    for item in results:
      self.assertEquals( item.title, "Foo" )
      self.assertEquals( item.content, "Bar" )


