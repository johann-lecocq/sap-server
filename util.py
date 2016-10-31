__author__ = "Johann Lecocq(johann-lecocq.fr)"
__license__ = "GNU GENERAL PUBLIC LICENSE version 2"

from json import dumps
from functools import wraps
from flask import make_response

class Reponse:
	""" representation of generic response with code and message"""
	def __init__(self,data,code=200):
		self.data=data
		self.code=code
	def to_json(self):
		return dumps(self.data)

class CrawlerReponse(Reponse):
	"""representation of reponse crawler(contains articles)"""
	def __init__(self,data,code=200):
		Reponse.__init__(self,data,code)
	def to_json(self):
		if len(self.data)==1:
			return dumps(article_to_json(self.data[0]))
		liste_articles=[]
		for article_ in self.data:
			liste_articles.append(article_to_json(article_))
		return dumps(liste_articles)


class InvalidCrawler(Exception):
	"""raise if crawler is unknow"""
	def __init__(self):
		Exception.__init__(self)

class InvalidParameter(Exception):
	"""raise when parameter are wrong"""
	def __init__(self):
		Exception.__init__(self)


def section_to_json(section_):
	"""Transformation Section object to simple python data
	Section -> dict"""
	section={"id":section_.identifiant}
	section["contents"]=[]
	for content_ in section_.content:
		section["contents"].append({"type":content_.type,"value":content_.value})
	return section

def article_to_json(article_):
	"""Transformation Article object to simple python data
	Article -> dict"""
	article=dict()
	article["id"]=article_.identifiant
	article["publish_date"]=article_.publish_date
	article["categorie"]=article_.categorie
	article["author"]=None
	article["sections"]=[]
	for section in article_.sections:
		article["sections"].append(section_to_json(section))
	return article

def render_json(func):
	"""Decorator to return JSON data
	Object(implement to_json) or simple python data -> str(JSON format)
	"""
	@wraps(func)
	def wrapper(*args, **kwargs):
		resultat=func(*args,**kwargs)
		if resultat.data==None:
			resp = make_response(dumps(None))
		else:
			resp = make_response(resultat.to_json())
		resp.status_code = resultat.code
		resp.headers['Content-type'] = 'application/json'
		return resp
	return wrapper

