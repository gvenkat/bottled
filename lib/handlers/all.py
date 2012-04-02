
from util.handler import Handler
from application import Application


class AllHandler( Handler ):

  def get(self):
    if not Application.has_been_setup():
      self.redirect( '/admin/setup' )
      return
    else:
      self.response.out.write('Hello world!')

  def post( self ):
    self.get()
