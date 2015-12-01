__author__ = "Johann Lecocq(johann-lecocq.fr)"
__license__ = "GNU GENERAL PUBLIC LICENSE version 2"
__version__ = "1.0"

from crawlerpy.vdm import VdmCrawler
from crawlerpy.dtc import DtcCrawler
from crawlerpy.scmb import ScmbCrawler

from util import InvalidCrawler

crawlers={"vdm":VdmCrawler(),
	"dtc":DtcCrawler(),
	"scmb":ScmbCrawler()
}

def select_crawler(c):
	"""return a crawler if is know"""
	global crawlers
	if c in crawlers:
		return crawlers[c]
	raise InvalidCrawler()

