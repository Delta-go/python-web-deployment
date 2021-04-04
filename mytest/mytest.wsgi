import sys

#app's path
sys.path.insert(0,"D:/mytest")

from mytest import app

#Initialize WSGI app object
application = app