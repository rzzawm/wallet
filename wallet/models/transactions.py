from . import db
from peewee import Model, CharField, FloatField, TimestampField, Check


class Transactions(Model):
    t_type = CharField(choices=["deposit", "withdraw"])
    description = CharField(max_length=127, null=True)
    amount = FloatField(constraints=[Check('amount > 0')])
    created_at = TimestampField()

    class Meta:
        database = db
