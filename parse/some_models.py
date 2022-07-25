from peewee import *

db = SqliteDatabase('towns.db')

class Towns(Model):
    count = IntegerField()
    town = CharField()
    district = CharField()
    OKATO = IntegerField()
    population = IntegerField()
    year_foundation = IntegerField()
    assignment_sity = IntegerField()
    icon = CharField()

    class Meta:
        database = db


Towns.create_table()