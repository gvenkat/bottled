
from util.handler import Handler

class AllHandler( Handler ):

  def get(self):
    self.response.out.write('Hello world!')

  def post( self ):
    self.get()
