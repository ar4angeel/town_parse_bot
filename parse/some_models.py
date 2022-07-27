from peewee import *

db = SqliteDatabase('towns.db')

class Towns(Model):
    count = IntegerField()
    town = CharField()
    district = CharField()
    okato = CharField()
    population = CharField()
    year_foundation = CharField()
    assignment_sity = CharField()

    class Meta:
        database = db


Towns.create_table()