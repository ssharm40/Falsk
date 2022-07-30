import traceback

from flask import Blueprint
from sqlorm.business_rules_configuration import business_rule_configuration
from src.config import engine
from sqlalchemy.orm import sessionmaker
from flask import Blueprint, jsonify, request
from src.models.model_configuration_modelling import ModelConfiguration


model_configuration= Blueprint('model_configuration', __name__)

modelconfiguration= ModelConfiguration()


@model_configuration.route('/save_business_rules_configuration', methods=['POST'])
def save_business_rules_configuration():
    try:
        request_data= request.get_json(force=True)
        business_rule_config= request_data['business_rule_config']

        status, message, code = modelconfiguration.save_business_rules_configuration(business_rule_config)

        if status=='success':
            
            return jsonify({
                   "status": status,
                   "message": message
                   
            }),code


    except Exception:
        print("Error Occured in API: save_business_rules_configuration : %s" % traceback.format_exc())
        response= {
            "status": "failure",
            "message": "JSON Structure is not correct"
        }
        return response, 400



@model_configuration.route('/get_business_rules-configuration', methods=['POST'])
def get_business_rules_configuration():
    try:
        status, model_attribute, attribute_items ,business_rule_configuration, code = modelconfiguration.get_business_rules_configuration()

        if status=='success':
            return jsonify({
                   "status": status,
                   "model_attribute": model_attribute,
                   "attribute_items": attribute_items,
                   "business_rule_configuration": business_rule_configuration
                   
            }),code
        elif status=='Failed':
            return jsonify({
                   "status": status,
                   "message": "Api Failed"
                   
            }),code

        return jsonify({
                "status":status,
                "business_rule_configuration": business_rule_configuration

        }),code

    except Exception:
        print("Error Occured in API: get_business_rules-configuration : %s" % traceback.format_exc())
        response= {
            "status": "failure",
            "message": "JSON Structure is not correct"
        }
        return response, 400


@model_configuration.route('/save_sla_configuration', methods=['POST'])
def save_sla_configuration():
    try:
        request_data= request.get_json(force=True)
        sla_config= request_data['sla_configuration']

        status, message, code = modelconfiguration.save_sla_configuration(sla_config)

        if status=='success':
            
            return jsonify({
                   "status": status,
                   "message": message
                   
            }),code
        elif status=='Failed':
            return jsonify({
                   "status": status,
                   "message": message
                   
            }),code


    except Exception:
        print("Error Occured in API: save_sla_configuration : %s" % traceback.format_exc())
        response= {
            "status": "failure",
            "message": "JSON Structure is not correct"
        }
        return response, 400

@model_configuration.route('/get_sla_configuration', methods=['POST'])
def get_sla_configuration():
    try:
        status, model_attribute, review_cycle_step, escalation_configuration, attribute_items, sla_config_data, code = modelconfiguration.get_sla_configuration()

        if status== 'success':
            return jsonify({
                   "status": status,
                   "model_attribute": model_attribute,
                   "review_cycle_step": review_cycle_step,
                   "escalation_configuration": escalation_configuration,
                   "attribute_items": attribute_items,
                   "sla_config_data": sla_config_data
                   
            }),code
        elif status=='Failed':
            return jsonify({
                   "status": status,
                   "model_attribute": model_attribute,
                   "review_cycle_step": review_cycle_step,
                   "escalation_configuration": escalation_configuration,
                   "attribute_items": attribute_items,
                   "sla_config_data": sla_config_data
                }),code


    except Exception:
        print("Error Occured in API: get_sla_configuration : %s" % traceback.format_exc())
        response= {
            "status": "failure",
            "message": "JSON Structure is not correct"
        }
        return response, 400        




@model_configuration.route('/save_workflow_configuration', methods=['POST'])
def save_workflow_configuration():
    try:
        request_data= request.get_json(force=True)
        workflow_config= request_data['workflow_config']

        status, message, code = modelconfiguration.save_workflow_configuration(workflow_config)

        if status=='success':
            return jsonify({
                   "status": status,
                   "message": message
                   
            }),code
        elif status=='Failed':
            return jsonify({
                   "status": status,
                   "message": message
                   
            }),code

    except Exception:
        print("Error Occured in API: save_workflow_configuration : %s" % traceback.format_exc())
        response= {
            "status": "failure",
            "message": "JSON Structure is not correct"
        }
        return response, 400


@model_configuration.route('/get_workflow_configuration', methods=['POST'])
def get_workflow_configuration():
    try:
        status,  workflow_configuration, code = modelconfiguration.get_workflow_configuration()

        if status=='success':
            return jsonify({
                   "status": status,
                   "workflow_configuration": workflow_configuration
                   
            }),code
        elif status=='Failed':
            return jsonify({
                   "status": status,
                   "message": "Api Failed"
                   
            }),code

    except Exception:
        print("Error Occured in API: get_workflow_configuration : %s" % traceback.format_exc())
        response= {
            "status": "failure",
            "message": "JSON Structure is not correct"
        }
        return response, 400


@model_configuration.route('/save_model', methods=['POST'])
def save_model():
    try:
        model_name = request.form['model_name']
        model_file= request.files['model_file']

        status, message, code = modelconfiguration.save_model(model_name, model_file)

        if status=='success':
            return jsonify({
                   "status": status,
                   "message": message
                   
            }),code
        elif status=='Failed':
            return jsonify({
                   "status": status,
                   "message": message
                   
            }),code
    except Exception:
        print("Error Occured in API: save_model : %s" % traceback.format_exc())
        response= {
            "status": "failure",
            "message": "JSON Structure is not correct"
        }
        return response, 400

    
@model_configuration.route('/file_details', methods=['POST'])
def file_details():
    try:
        model_data = request.form['model_data']
        print("Model has been uploade")
        status, message, code = modelconfiguration.file_details(model_name)

        if status=='success':
            return jsonify({
                   "status": status,
                   "message": message
                   
            }),code
        elif status=='Failed':
            return jsonify({
                   "status": status,
                   "message": message
                   
            }),code
    except Exception:
        print("Error Occured in API: file_details : %s" % traceback.format_exc())
        response= {
            "status": "failure",
            "message": "JSON Structure is not correct"
        }
        return response, 400
        
