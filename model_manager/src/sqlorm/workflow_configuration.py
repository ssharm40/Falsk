from marshmallow import fields
from . import db, ma
from datetime import datetime

class workflow_configuration(db.Model):
    __tablename__ = 'workflow_configuration'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    wf_id= db.Column(db.Integer, nullable=False)
    wf_name= db.Column(db.String(255), nullable=False)
    wf_desc = db.Column(db.String(255), nullable=False)
    from_status= db.Column(db.String(255), nullable=False)
    to_status = db.Column(db.String(255), nullable=False)
    responsiblity= db.Column(db.String(255), nullable=False)
    wf_seq = db.Column(db.Integer, nullable=False)
    review_only= db.Column(db.String(255), nullable=False)
    wf_type = db.Column(db.String(255), nullable=False)
    create_by= db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    date_modified = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())


    def add(self):
        db.session.add(self)
        db.session.commit()


    def rollback(self):
        db.session.rollback()




class workflow_configurationSchema(ma.Schema):
    id = fields.Integer()
    wf_id = fields.Integer()
    wf_name = fields.String()
    wf_desc = fields.String()
    from_status = fields.String()
    to_status = fields.String()
    responsiblity = fields.String()
    wf_seq = fields.Integer()
    review_only = fields.String()
    wf_type = fields.String()
    create_by = fields.String()
    date_created = fields.DateTime()
    date_modified = fields.DateTime()
    


    