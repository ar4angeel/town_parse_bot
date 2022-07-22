from peewee import *

db = SqliteDatabase('towns.db')

class Towns(Model):
    count = IntegerField()
    town = CharField()
    district = CharField()
    OKATO = IntegerField()
    population = IntegerField()
    year_foundation = IntegerField()
    asignment_sity = IntegerField()
    icon =
