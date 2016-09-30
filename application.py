__author__ = "Johann Lecocq(johann-lecocq.fr)"
__license__ = "GNU GENERAL PUBLIC LICENSE version 2"
__version__ = "1.0"

from flask import Blueprint

from service import select_crawler
from util import *

routes = Blueprint('routes', __name__)

@routes.route('/<crawler>/articles/<identifiant>', methods = ['GET'])
@render_json
def article(crawler,identifiant=""):
	"""get an article with id"""
	if identifiant=="":
		raise InvalidParameter()
	crawler=select_crawler(crawler)
	resultat=crawler.article(identifiant)
	return CrawlerReponse(resultat.data,code=resultat.code)

@routes.route('/<crawler>/pages/<int:numero>', methods = ['GET'])
@render_json
def pages(crawler,numero=0):
	"""get articles of an page with id page"""
	if numero < 0:
		raise InvalidParameter()
	crawler=select_crawler(crawler)
	resultat=crawler.page(numero)
	return CrawlerReponse(resultat.data,code=resultat.code)
	
@routes.route('/<crawler>/random',methods = ['GET'])
@render_json
def random(crawler):
	"""get a random article"""
	crawler=select_crawler(crawler)
	resultat=crawler.article_random()
	return CrawlerReponse(resultat.data,code=resultat.code)

@routes.route('/<crawler>/archives/<int:annee>/<int:mois>',methods=['GET'])
@render_json
def archives_mois(crawler,annee,mois):
	"""get articles on archives year + month
	not implemented -> crawlers can't get articles by archives"""
	return Reponse(None,code=501)

@routes.route('/<crawler>/archives/<int:annee>/<int:mois>/<int:jour>',methods=['GET'])
@render_json
def archives_jour(crawler,annee,mois,jour):
	"""get articles on archives year + month + day
	not implemented -> crawlers can't get articles by archives"""
	return Reponse(None,code=501)

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
