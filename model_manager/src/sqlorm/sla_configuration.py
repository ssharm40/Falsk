from marshmallow import fields
from . import db, ma
from datetime import datetime

class sla_configuration(db.Model):
    __tablename__ = 'sla_configuration'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    master_id = db.Column(db.Integer, nullable=False)
    model_attribute= db.Column(db.String, nullable=False)
    attribute_items= db.Column(db.String, nullable=False)
    review_cycle_step = db.Column(db.String, nullable=False)
    thresold = db.Column(db.Integer, nullable=False)
    escalation = db.Column(db.Integer, default=10)
    escalation_frequency = db.Column(db.String, nullable=False)
    to_user= db.Column(db.String, nullable=False)
    cc_user = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    create_by = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    date_modified = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
     

    def add(self):
        db.session.add(self)
        db.session.commit()


    def rollback(self):
        db.session.rollback()



class sla_configurationSchema(ma.Schema):
    id = fields.Integer()
    master_id = fields.Integer()
    model_attribute = fields.String()
    attribute_items = fields.String()
    review_cycle_step = fields.String()
    thresold = fields.Integer()
    escalation = fields.Integer()
    escalation_frequency = fields.String()
    to_user = fields.String()
    cc_user = fields.String()
    status = fields.String()
    create_by = fields.String()
    date_created = fields.DateTime()
    date_modified = fields.DateTime()
        