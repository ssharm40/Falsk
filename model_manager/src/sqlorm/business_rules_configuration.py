from marshmallow import fields
from . import db, ma 
from datetime import datetime

class business_rule_configuration(db.Model):
    __tablename__ = 'business_rule_configuration'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    master_id = db.Column(db.Integer, nullable=False)
    model_attribute = db.Column(db.String(255), nullable=False)
    attribute_items = db.Column(db.String(255), nullable=False)
    workflow_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(255), nullable=False)
    created_by = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    date_modified = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())



    def add(self):
        db.session.add(self)
        db.session.commit()

    def rollback(self):
        db.session.rollback()


class business_rule_configurationSchema(ma.Schema):
    id = fields.Integer()
    master_id = fields.Integer()        
    model_attribute = fields.String()
    attribute_items = fields.String()
    workflow_id = fields.Integer()
    status = fields.String()
    created_by = fields.String()
    date_created = fields.DateTime()
    date_modified = fields.DateTime()


    


