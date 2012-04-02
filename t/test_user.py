import sys,unittest
from os.path import dirname

sys.path.append( dirname( __file__ ) + '/../lib' )

from util import apptest
from model.user import User
from google.appengine.api import users


class UserTestCase( apptest.BottledTestCase ):

  def testNonExistance( self ):
    user = users.get_current_user()
    self.isNone( user )

  def testExistance( self ):
    self.setup_user()
    user = users.get_current_user()
    self.isNotNone( user )
    self.assertEquals( user.email(), 'foo@bar.com' )

  def testNonAdminUser( self ):
    self.setup_user()
    user = users.get_current_user()
    self.isNotNone( user )
    self.assertEquals( user.email(), 'foo@bar.com' )
    self.assert_( users.is_current_user_admin() is not True )


  def testAdminUser( self ):
    self.setup_admin_user()
    user = users.get_current_user()
    self.isNotNone( user )
    self.assertEquals( user.email(), 'foo@bar.com' )
    self.assert_( users.is_current_user_admin() is True )




