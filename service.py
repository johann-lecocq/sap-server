__author__ = "Johann Lecocq(johann-lecocq.fr)"
__license__ = "GNU GENERAL PUBLIC LICENSE version 2"

from crawlerpy.vdm import VdmCrawler
from crawlerpy.dtc import DtcCrawler
from crawlerpy.scmb import ScmbCrawler

from util import *
CHEMIN_IMAGE="image"

CRAWLERS={"vdm":{"crawler":VdmCrawler(),"information":{
                "image":"/vdm/image","titre":"Vie de merde","acronyme":"VDM",
                "description":"VDM - VieDeMerde : Prenez la vie côté humour en partageant vos petits malheurs et drôles d'histoires de la vie quotidienne, car ça fait du bien d'en rire."
                }
        },
        "dtc":{"crawler":DtcCrawler(),"information":{
                "image":"/scmb/image","titre":"Dans ton chat","acronyme":"DTC",
                "description":"Dans Ton Chat, c'est le site qui recense les extraits de conversation (quotes) les plus drôles, tirés de vos dialogues sur internet. Oui, c'est un peu comme des brèves de comptoir, mais avec des geeks, et de l'interactivité."
                }
        },
        "scmb":{"crawler":ScmbCrawler(),"information":{
                "image":"/scmb/image","titre":"Se coucher moins bete","acronyme":"SCMB","description":"Vous allez briller en soirée"
                }
        }
}

def select_crawler(c):
    """return a crawler if is know"""
    if c in CRAWLERS:
        return CRAWLERS[c]["crawler"]
    raise InvalidCrawler()

def article(crawler,identifiant):
    """get an article with id"""
    crawler=select_crawler(crawler)
    resultat=crawler.article(identifiant)
    return CrawlerReponse(resultat.data,code=resultat.code)

def pages(crawler,numero):
    """get articles of an page with id page"""
    crawler=select_crawler(crawler)
    resultat=crawler.page(numero)
    return CrawlerReponse(resultat.data,code=resultat.code)

def random(crawler):
    """get a random article"""
    crawler=select_crawler(crawler)
    resultat=crawler.article_random()
    return CrawlerReponse(resultat.data,code=resultat.code)

def archives_mois(crawler,annee,mois):
    """get articles on archives year + month
    not implemented -> crawlers can't get articles by archives"""
    return Reponse(None,code=501)

def archives_jour(crawler,annee,mois,jour):
    """get articles on archives year + month + day
    not implemented -> crawlers can't get articles by archives"""
    return Reponse(None,code=501)

def information(crawler):
    if crawler not in CRAWLERS:
        raise InvalidCrawler()
    return Reponse(CRAWLERS[crawler]["information"],code=200)

def chemin_image(crawler):
    if crawler not in CRAWLERS:
        raise InvalidCrawler()
    return CRAWLERS[crawler]["information"]["image"]
    
