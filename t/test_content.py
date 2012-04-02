
import sys,unittest
from os.path import dirname

sys.path.append( dirname( __file__ ) + '/../lib' )

from util import apptest
from model import content

class ContentTestCase( apptest.BottledTestCase ):
  def testFoo( self ):
    self.assert_( True )
