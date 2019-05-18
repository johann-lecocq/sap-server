from crawlerpy.vdm import VdmCrawler
from crawlerpy.dtc import DtcCrawler
from crawlerpy.scmb import ScmbCrawler

logo_path = "image"

crawlers = {
    "vdm": {
        "crawler": VdmCrawler(),
        "information": {
            "image": "/vdm/image",
            "titre": "Vie de merde", "acronyme": "VDM",
            "description": "VDM - VieDeMerde : Prenez la vie côté humour en partageant vos petits malheurs et drôles d'histoires de la vie quotidienne, car ça fait du bien d'en rire."
        }
    },
    "dtc": {
        "crawler": DtcCrawler(),
        "information": {
            "image": "/scmb/image",
            "titre": "Dans ton chat", "acronyme": "DTC",
            "description": "Dans Ton Chat, c'est le site qui recense les extraits de conversation (quotes) les plus drôles, tirés de vos dialogues sur internet. Oui, c'est un peu comme des brèves de comptoir, mais avec des geeks, et de l'interactivité."
        }
    },
    "scmb": {
        "crawler": ScmbCrawler(),
        "information": {
            "image": "/scmb/image",
            "titre": "Se coucher moins bete", "acronyme": "SCMB", "description": "Vous allez briller en soirée"
        }
    }
}