#!/usr/bin/env python

import sys
from os.path import dirname

sys.path.insert( 0, dirname( __file__ ) + '/lib' )

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from handlers import admin, all
from handlers.admin import *


def main():

  application = webapp.WSGIApplication(
    [
      ( '/admin/setup',   setup.Setup ),
      ( '/admin/?.*',     index.AdminHandler ),
      ( '/.*',            all.AllHandler )
    ],

    debug=True
  )

  # Run WSGI
  util.run_wsgi_app(application)


# Main shit
if __name__ == '__main__':
    main()
