__author__ = "Johann Lecocq(johann-lecocq.fr)"
__license__ = "GNU GENERAL PUBLIC LICENSE version 2"
__version__ = "1.0"

import cherrypy
from paste.translogger import TransLogger

from application import app

if __name__ == "__main__":
	app_logged = TransLogger(app)
	cherrypy.tree.graft(app_logged, '/')
	cherrypy.config.update({
		'engine.autoreload.on': False,
		'log.screen': True,
		'server.socket_port': 8007,
		'server.socket_host': '0.0.0.0'
	})
	cherrypy.engine.start()
	cherrypy.engine.block()

