import traceback

import dateutil.parser
from matplotlib.style import available
from requests import session
from sqlorm.master_data_config import master_data_config
from sqlorm.workflow_configuration import workflow_configuration

from src import sqlorm
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from src.config import engine
from datetime import datetime
from configparser import ConfigParser
import os
from sqlalchemy.sql.expression import func



create_time= datetime.utcnow()

class ModelConfiguration:
    def __init__(self):
        pass


    def save_business_rules_configuration(self, business_rule_config):
        try:
            for data in business_rule_config:
                model_attribute= data['model_attribute']
                attribute_items= data['attribute_items']
                workflow= data['workflow']

            master_data_config_query= sqlorm.master_data_config.query.filter_by(keys= str(model_attribute), values= str(attribute_items)).first()

            workflow_id_query= sqlorm.workflow_configuration.query.with_entities(sqlorm.workflow_configuration.wf_id).filter_by(workflow_name= str(workflow)).first()


            if not master_data_config_query and not workflow_id_query:
                return "Failed", "Data Not Present in Master_data_table", 400
            else:
                master_id= int(master_data_config_query.id)
                workflow_id = int(workflow_id_query.wf_id)

            buss_rule_details= sqlorm.business_rule_configuration(master_id=master_id, model_attribute=model_attribute, attribute_items= attribute_items, workflow_id= workflow_id, status= 'Active',created_by="Admin1", date_created= create_time, date_modified= create_time)

            buss_rule_details.add()

            return "Success", "Data Saved Successfully", 200

                      
        except Exception:
            print("Error Occured in API: save_business_rules_configuration : %s" % traceback.format_exc())
            business_rule_configuration= sqlorm.business_rule_configuration()
            business_rule_configuration.rollback()
            return "Failed", "Record Not Inserted", 400



    def get_business_rules_configuration(self):
        try:
            # Feteching all the model_attribute from master_key_value tables

            result_mk= sqlorm.master_data_config.query.filter_by(keys= 'model_attribute')
            result_mk_count= session.query(result_mk.exists()).scalar()

            model_attribute= []
            if result_mk_count:
                for j in result_mk:
                    model_attribute.append(str(j.values))

            #Fetching all the attribute_items for the corresponding model_attribute from master_key_value tables
            attribute_items={}
            for keys in model_attribute:
                result_mk= sqlorm.master_data_config.query.filter_by(keys= keys.lower())
                key_value=[]
                for j in result_mk:
                    key_value.append(str(j.values))
                attribute_items[keys]= key_value

            # Fetching all the business rule config details from business_rule_configuration table  

            buss_config_details= sqlorm.business_rule_configuration.query.all()

            if not buss_config_details:
                buss_config_details= [{"model_attribute": "", "attribute_items": "", "workflow": "", "status": "", "created_by": "", "date_created": ""}]
            else:
                buss_config_details= [{"model_attribute": str(i.model_attribute), "attribute_items": str(i.attribute_items), "workflow": str(i.workflow_id), "status": str(i.status), "created_by": str(i.created_by), "date_created": str(i.date_created)} for i in buss_config_details]

            return "Success",model_attribute ,attribute_items,buss_config_details, 200
            

        except Exception:
            print("Error Occured in API: get_business_rules_configuration : %s" % traceback.format_exc())
            return "Failed", "Record Not Found", "Not Found",400

    def save_sla_configuration(self, sla_config):
        try:
            for data in sla_config:
                model_attribute= data['model_attribute']
                attribute_items= data['attribute_items']
                review_cycle_step= data['review_cycle_step']
                thresold= data['thresold']
                escalation= data['escalation']
                escalation_frequency = data['escalation_frequency']
                to_user = data['to_user']
                cc_user = data['cc_user']


            master_data_config_query= sqlorm.master_data_config.query.filter_by(keys= str(model_attribute), values= str(attribute_items)).first()

            if not master_data_config_query:
                return "Failed", "Data Not Present in Master_data_table", 400

            else:
                master_id= int(master_data_config_query.id)

            sla_config_details= sqlorm.sla_configuration(master_id=master_id, model_attribute=model_attribute, attribute_items= attribute_items, review_cycle_step= review_cycle_step, thresold= thresold, escalation= escalation, escalation_frequency= escalation_frequency, to_user= to_user, cc_user= cc_user, status= 'Active',created_by="Admin1")

            sla_config_details.add()

            print("API SLA Configuration has been added successfully")
            return "Success", "Data Saved Successfully", 200
                        
        except Exception:
            print("Error Occured in API: save_sla_configuration : %s" % traceback.format_exc())
            return "Failed", "Record Not Inserted", 400

    def get_sla_configuration(self):
        try:
            # Fetching all the model_attributes, Review Cycle step, Escalation Frequency from master data config

            result_mk= sqlorm.master_data_config_query.filter( (sqlorm.master_data_config.keys== 'moelel_attribute') | (sqlorm.master_data_config.keys=="review_cycle_step")|(sqlorm.master_data_config.keys=="escalation_frequency"))

            result_mk_count= session.query(result_mk.exists()).scalar()

            model_attribute= []
            review_cycle_step= []
            escalation_frequency= []
            if result_mk_count:
                for j in result_mk:
                    if j.keys== 'model_attribute':
                        model_attribute.append(str(j.values))
                    elif j.keys== 'review_cycle_step':
                        review_cycle_step.append(str(j.values))
                    elif j.keys== 'escalation_frequency':
                        escalation_frequency.append(str(j.values))

            # Fetching all the attribute_items for the corresponding model_attribute from master_data_config table

            attribute_items={}
            for keys in model_attribute:
                result_mk= sqlorm.master_data_config.query.filter_by(keys= keys.lower())
                key_value=[]
                for j in result_mk:
                    key_value.append(str(j.values))
                attribute_items[keys]= key_value

            # Fetching all the sla config details from sla_configuration table
            sla_config_details= sqlorm.sla_configuration.query.all()

            if not sla_config_details:
                sla_config_details= [{"model_attribute": "", "attribute_items": "", "review_cycle_step": "", "thresold": "", "escalation": "", "escalation_frequency": "", "to_user": "", "cc_user": "", "status": "", "created_by": "", "date_created": ""}]
            else:
                sla_config_details= [{"model_attribute": str(i.model_attribute), "attribute_items": str(i.attribute_items), "review_cycle_step": str(i.review_cycle_step), "thresold": str(i.thresold), "escalation": str(i.escalation), "escalation_frequency": str(i.escalation_frequency), "to_user": str(i.to_user), "cc_user": str(i.cc_user), "status": str(i.status), "created_by": str(i.created_by), "date_created": str(i.date_created)} for i in sla_config_details]

            return "Success",model_attribute ,attribute_items,review_cycle_step,escalation_frequency,sla_config_details, 200
        except Exception:
            print("Error Occured in API: get_sla_configuration : %s" % traceback.format_exc())
            return "Failed", "Record Not Found", "Not Found",400

    def save_workflow_configuration(self, workflow_config):
        try:
            for data in workflow_config:
                wf_name= data['wf_name']
                wf_desc= data['wf_desc']
                from_status= data['from_status']
                to_status= data['to_status']
                responsiblity= data['responsiblity']
                review_only= data['review_only']
                wf_type= data['wf_type']
            
            wf_id_query= sqlorm.workflow_configuration.query.with_entities(sqlorm.workflow_configuration.wf_id).filter_by(wf_name= wf_name).first()

            if not wf_id_query:
                # For new Workflow Configuration
                max_id= session.query(func.max(sqlorm.workflow_configuration.wf_id)).scalar()

                if not max_id:
                    # IF database is blank
                    wf_seq= 1
                    wf_id= max_id+1
            else:

                #For exist workflow

                wf_id= wf_id_query.wf_id
                wf_seq= session.query(func.max(sqlorm.workflow_configuration.wf_seq)).filter(sqlorm.workflow_configuration.wf_name== wf_id).scalar()+1


            workflow_config_details= sqlorm.workflow_configuration(wf_id=wf_id, wf_name= wf_name, wf_desc= wf_desc, from_status= from_status, to_status= to_status, responsiblity= responsiblity, review_only= review_only, wf_type= wf_type, wf_seq= wf_seq, status= 'Active',created_by="Admin1") 
            workflow_config_details.add()

            print("API Workflow Configuration has been added successfully")

            return "Success", "Data Saved Successfully", 200
            


            





        except Exception:
            print("Error Occured in API: save_workflow_configuration : %s" % traceback.format_exc())
            workflow_configuration= sqlorm.workflow_configuration()
            workflow_configuration.rollback()
            return "Failed", "Record Not Inserted", 400

    def get_workflow_configuration(self):
        try:
            # Fetching all the workflow config details from workflow_configuration table
            workflow_config_details= sqlorm.workflow_configuration.query.all()

            if not workflow_config_details:
                workflow_config_details= [{"wf_id": "", "wf_name": "", "wf_desc": "", "from_status": "", "to_status": "", "responsiblity": "", "review_only": "", "wf_type": "", "wf_seq": "", "status": "", "created_by": "", "date_created": ""}]
            else:
                workflow_config_details= [{"wf_id": str(i.wf_id), "wf_name": str(i.wf_name), "wf_desc": str(i.wf_desc), "from_status": str(i.from_status), "to_status": str(i.to_status), "responsiblity": str(i.responsiblity), "review_only": str(i.review_only), "wf_type": str(i.wf_type), "wf_seq": str(i.wf_seq), "status": str(i.status), "created_by": str(i.created_by), "date_created": str(i.date_created)} for i in workflow_config_details]

            return "Success", workflow_config_details, 200
        except Exception:
            print("Error Occured in API: get_workflow_configuration : %s" % traceback.format_exc())
            return "Failed", "Record Not Found", "Not Found",400        

    def save_model(self, model_name, model_file):
        try:
            import datetime

            save_path= "C:/ModuleManager/model_manager/files"

            file_ext= os.path.splittext(model_file.filename)[1]

            if file_ext in ['.xlsx', '.xls', '.csv']:
                today= datetime.datetime.now()
                year= str(today.year)

                month_name_object= datetime.datetime.strptime(str(today.month), '%m')
                month= month_name_object.strftime("%B")

                available_year_folders= os.listdir(save_path)

                save_path= save_path+"/"+year

                if year not in available_year_folders:
                    os.mkdir(save_path)

                # Available month folders in the year folder
                available_month_folders= os.listdir(save_path)
                
                save_path= save_path+"/"+ month

                if month not in available_month_folders:
                    os.mkdir(save_path)

                
                # Available model folders in the month folder
                available_model_folders= os.listdir(save_path)
                save_path= save_path+"/"+ model_name

                if model_name not in available_model_folders:
                    os.mkdir(save_path)

                available_files= os.listdir(save_path)

                #csv xls xlsx

                if model_file.filename.replace(" ", "_") in available_files:
                    print("File already exists with the same name")
                    return "Failed", "Model Already Exists", 400

                else:
                    model_file.save(os.path.join(save_path, secure_filename(model_file.filename)))

                print("Model has been saved successfully")
                return "Success", "Model Saved Successfully", 200
            else:
                print("File format not supported \nSupported formats are .csv, .xls, .xlsx")
                return "Failed", "File Format Not Supported", 400
                

        except Exception:
            print("Error Occured in API: save_model : %s" % traceback.format_exc())
            return "Failed", "File not saved", 400


    def file_details():
        pass

