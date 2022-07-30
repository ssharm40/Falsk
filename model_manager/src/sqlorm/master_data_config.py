from marshmallow import fields
from .db import db, ma


class master_data_config(db.Model):
    __tablename__ = 'master_data_config'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    keys= db.Column(db.String(255), nullable=False)
    values= db.Column(db.String(255), nullable=False)


    def add(self):
        db.session.add(self)
        db.session.commit()

    def rollback(self):
        db.session.rollback()


class master_data_configSchema(ma.Schema):
    id = fields.Integer()
    keys = fields.String()
    values = fields.String()

    