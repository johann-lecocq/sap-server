__author__ = "Johann Lecocq(johann-lecocq.fr)"
__license__ = "GNU GENERAL PUBLIC LICENSE version 2"

from flask import Blueprint,send_from_directory

import service
from util import *

routes = Blueprint('routes', __name__)

@routes.route('/<crawler>/articles/<identifiant>', methods = ['GET'])
@render_json
def article(crawler,identifiant=""):
    if identifiant=="":
        raise InvalidParameter()
    return service.article(crawler,identifiant)

@routes.route('/<crawler>/pages/<int:numero>', methods = ['GET'])
@render_json
def pages(crawler,numero=0):
    if numero < 0:
        raise InvalidParameter()
    return service.pages(crawler,numero)
    
@routes.route('/<crawler>/random',methods = ['GET'])
@render_json
def random(crawler):
    return service.random(crawler)

@routes.route("/<crawler>/random_one",methods=["GET"])
@render_json
def random_one(crawler):
    return service.random_one(crawler)

@routes.route('/<crawler>/archives/<int:annee>/<int:mois>',methods=['GET'])
@render_json
def archives_mois(crawler,annee,mois):
    return service.archives_mois(crawler,annee,mois)

@routes.route('/<crawler>/archives/<int:annee>/<int:mois>/<int:jour>',methods=['GET'])
@render_json
def archives_jour(crawler,annee,mois,jour):
    return service.archives_jour(crawler,annee,mois,jour)

@routes.route('/<crawler>',methods=['GET'])
@render_json
def information(crawler):
    return service.information(crawler)

@routes.route('/<crawler>/image',methods=['GET'])
def image(crawler):
    service.select_crawler(crawler)
    return send_from_directory("image",crawler+".png", as_attachment=False)


@routes.errorhandler(InvalidCrawler)
@render_json
def handle_invalid_crawler(error):
    """return a code 500 when the crawler is unknow"""
    return Reponse("Invalid crawler",code=500)

@routes.errorhandler(InvalidParameter)
@render_json
def handle_invalid_parameter(error):
    """return a 400 code when the parameter are not good"""
    return Reponse("Invalid parameter",code=400)
