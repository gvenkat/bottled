import unittest
from google.appengine.ext import testbed


class BottledTestCase( unittest.TestCase ):

  def setUp( self ):
    self.testbed = testbed.Testbed()
    self.testbed.activate()
    self.testbed.init_mail_stub()

    # FIXME: Cannot hardcode the tests
    self.testbed.setup_env(app_id='bottled')

    self.testbed.init_datastore_v3_stub()
    self.testbed.init_blobstore_stub()

  def isNone( self, obj ):
    self.assert_( obj is None )

  def isNotNone( self, obj ):
    self.assert_( obj is not None )

  def isFalse( self, obj ):
    self.assert_( obj == False )

  def isTrue( self, obj ):
    self.assert_( obj == True )

  def tearDown( self ):
    self.testbed.deactivate()

