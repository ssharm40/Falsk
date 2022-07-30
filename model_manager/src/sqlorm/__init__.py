from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma= Marshmallow()
db= SQLAlchemy()

from .business_rules_configuration import business_rule_configuration, business_rule_configurationSchema
from .workflow_configuration import workflow_configuration, workflow_configurationSchema
from .master_data_config import master_data_configuration, master_data_configurationSchema


