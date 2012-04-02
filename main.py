#!/usr/bin/env python

import sys
from os.path import dirname

sys.path.insert( 0, dirname( __file__ ) + '/lib' )

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from handlers import *

def main():

  application = webapp.WSGIApplication(
    [
      ( '/admin/*', admin.AdminHandler ),
      ( '/',        all.AllHandler )
    ],

    debug=True
  )

  # Run WSGI
  util.run_wsgi_app(application)


# Main shit
if __name__ == '__main__':
    main()
