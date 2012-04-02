import sys
import unittest
from os.path import dirname

sys.path.append( dirname( __file__ ) + '/../lib' )

from util import apptest
from model.setting import Setting
from application import Application

class SettingTestCase( apptest.BottledTestCase ):

  def testAppSetup( self ):
    self.assert_( Setting.is_app_setup() == False )
    self.assert_( Application.has_been_setup() == False )

    Setting(
      app_name = 'Foobar',
      app_version = 0.01,
      allow_registration = True
    ).put()

    self.assert_( Setting.is_app_setup() == True )
    self.assert_( Application.has_been_setup() == True )


  def testDestroy( self ):
    pass




