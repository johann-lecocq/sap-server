from flask import Flask, send_from_directory, jsonify

from exceptions import *
from config import crawlers
from schema import ArticleSchema

app = Flask("sap")

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

def select_crawler(c):
    """return a crawler if is know"""
    if c in crawlers:
        return crawlers[c]["crawler"]
    raise InvalidCrawler()


@app.errorhandler(InvalidCrawler)
def handle_invalid_crawler(error):
    """return a code 500 when the crawler is unknow"""
    return "Invalid crawler", 500


@app.errorhandler(InvalidParameter)
def handle_invalid_parameter(error):
    """return a 400 code when the parameter are not good"""
    return "Invalid parameter", 400


@app.route('/<crawler>/articles/<identifiant>', methods=['GET'])
def article(crawler, identifiant=""):
    code, result = select_crawler(crawler).article(identifiant)
    return jsonify(article_schema.dump(result)), code


@app.route('/<crawler>/pages/<int:number>', methods=['GET'])
def page(crawler, number=0):
    if number < 0:
        raise InvalidParameter()
    code, result=select_crawler(crawler).page(number)
    return jsonify(articles_schema.dump(result)), code


@app.route('/<crawler>/random', methods=['GET'])
def random(crawler):
    code, result=select_crawler(crawler).random()
    return jsonify(articles_schema.dump(result)), code


@app.route('/<crawler>', methods=['GET'])
def information(crawler):
    select_crawler(crawler)
    return crawlers[crawler]["information"], 200


@app.route('/<crawler>/image', methods=['GET'])
def image(crawler):
    select_crawler(crawler)
    return send_from_directory("image", crawler+".png", as_attachment=False)
