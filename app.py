from bottle import route, install, template, run
from bottle_sqlite import SQLitePlugin

install(SQLitePlugin(dbfile='/database/horarios.db'))

import routes

run (host='0.0.0.0', port=8080, debug=True, reloader=True)
