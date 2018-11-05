activate_this = '/var/www/demo/.venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os
#user = "demo"
#password = "demo"
#server/sqlinstance = mysql-db-1/demo
os.environ['DATABASE_URI'] = 'mysql://demo:demo@mysql-db-1/demo'

import sys
sys.path.insert(0, '/var/www/demo')

from demo import app as application
