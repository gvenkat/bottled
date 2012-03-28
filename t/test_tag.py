import sys
import unittest
from os.path import dirname

sys.path.append( dirname( __file__ ) + '/../lib' )

from util import apptest
from model.tag import Tag

class TagTestCase( apptest.BottledTestCase ):

  def testBasic( self ):
    a = Tag( tag="ios" )

    self.isNotNone( a )
    self.assertEqual( "ios", a.tag )
    self.assertEqual( Tag.count(), 0 )


  def testCreate( self ):
    Tag( tag="ios" ).put()
    Tag( tag="perl" ).put()
    Tag( tag="javascript" ).put()

    self.assertEqual( Tag.count(), 3 )

    Tag( tag="ruby" ).put()

    self.assertNotEqual( Tag.count(), 3 )
    self.assertEqual( Tag.count(), 4 )


  def testFetch( self ):
    Tag( tag="ruby" ).put()
    Tag( tag="javascript" ).put()
    Tag( tag="perl" ).put()
    self.assertEqual( Tag.count(), 3 )
    self.assertEqual( len( Tag.all_tags() ), 3 )

