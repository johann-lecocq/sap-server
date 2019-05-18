from lima import Schema
from lima.fields import String, Date, Embed
from crawlerpy.sap import Article, Section, Data

class DataSchema(Schema):
    type = String()
    value = String()

class SectionSchema(Schema):
    id = String()
    contents = Embed(schema=DataSchema, many=True)

class ArticleSchema(Schema):
    id = String()
    publish_date = String()
    categorie = String()
    sections = Embed(schema=SectionSchema, many=True)

