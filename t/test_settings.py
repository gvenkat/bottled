import sys
import unittest
from os.path import dirname

sys.path.append( dirname( __file__ ) + '/../lib' )

from util import apptest
from model.setting import Setting

class SettingTestCase( apptest.BottledTestCase ):

  def testBasic( self ):

    setting = Setting(
      app_name='Foobar',
      app_version=0.01,
      allow_registration=False
    )

    self.isNotNone( setting )
    self.assertEqual( setting.app_name, 'Foobar' )
    self.assertAlmostEquals( setting.app_version, 0.01 )
    self.isFalse( setting.allow_registration )

  def testCreate( self ):

    setting = Setting(
      app_name = 'Foobar',
      app_version = 0.01,
      allow_registration = True
    )

    setting.put()

    self.assertEqual( Setting.all().count(), 1 )


  def testClassAccessors( self ):
    setting = Setting(
      app_name = 'Foobar',
      app_version = 0.01,
      allow_registration = True
    )

    setting.put()

    self.assertEqual( Setting.all().count(), 1 )
    self.assertEqual( Setting.name(), 'Foobar' )
    self.assertEqual( Setting.version(), '0.01' )


  def testAppSetup( self ):
    # Setting.all().get().delete()

    self.assert_( Setting.is_app_setup() == False )

    Setting(
      app_name = 'Foobar',
      app_version = 0.01,
      allow_registration = True
    ).put()

    self.assert_( Setting.is_app_setup() == True )


  def testDestroy( self ):
    pass




