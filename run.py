__author__ = "Johann Lecocq(johann-lecocq.fr)"
__license__ = "GNU GENERAL PUBLIC LICENSE version 2"
__version__ = "1.0"

import cherrypy
from paste.translogger import TransLogger
from flask import Flask

from application import routes

if __name__ == "__main__":
    app = Flask("sap")
    app.register_blueprint(routes)
    app_logged = TransLogger(app)
    cherrypy.tree.graft(app_logged, '/')
    cherrypy.config.update({
        'engine.autoreload.on': False,
        'log.screen': True,
        'server.socket_port': 8007,
        'server.socket_host': '127.0.0.1'
    })
    cherrypy.engine.start()
    cherrypy.engine.block()

