"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import requests, json
from connectors.core.connector import get_logger, ConnectorError
from .constants import *

logger = get_logger('illumio-core')


class Illumio(object):
    def __init__(self, config, *args, **kwargs):
        self.api_key = config.get('api_key')
        self.api_token = config.get('api_token')
        url = config.get('server_url').strip('/')
        if not url.startswith('https://') and not url.startswith('http://'):
            self.url = 'https://{0}/api/v2'.format(url)
        else:
            self.url = url + '/api/v2'
        self.verify_ssl = config.get('verify_ssl')

    def make_rest_call(self, endpoint, method, data=None, params=None):
        try:
            url = self.url + endpoint
            headers = {
                'Content-Type': 'application/json'
            }
            logger.debug("Endpoint {0}".format(url))
            response = requests.request(method, url, data=data, params=params, auth=(self.api_key, self.api_token),
                                        headers=headers, verify=self.verify_ssl)
            logger.debug("response_content {0}:{1}".format(response.status_code, response.content))
            if response.ok or response.status_code == 204:
                logger.info('Successfully got response for url {0}'.format(url))
                if 'json' in str(response.headers):
                    return response.json()
                else:
                    return response
            else:
                logger.error("{0}".format(response.status_code))
                raise ConnectorError("{0}:{1}".format(response.status_code, response.text))
        except requests.exceptions.SSLError:
            raise ConnectorError('SSL certificate validation failed')
        except requests.exceptions.ConnectTimeout:
            raise ConnectorError('The request timed out while trying to connect to the server')
        except requests.exceptions.ReadTimeout:
            raise ConnectorError(
                'The server did not send any data in the allotted amount of time')
        except requests.exceptions.ConnectionError:
            raise ConnectorError('Invalid Credentials')
        except Exception as err:
            raise ConnectorError(str(err))


def check_payload(payload):
    updated_payload = {}
    for key, value in payload.items():
        if isinstance(value, dict):
            nested = check_payload(value)
            if len(nested.keys()) > 0:
                updated_payload[key] = nested
        elif value != '' and value is not None:
            updated_payload[key] = value
    return updated_payload


def create_workload(config, params):
    try:
        il = Illumio(config)
        endpoint = '/orgs/{0}/workloads'.format(params.get('org_id'))
        payload = {
            'name': params.get('name'),
            'description': params.get('description'),
            'hostname': params.get('hostname'),
            'service_principal_name': params.get('service_principal_name'),
            'public_ip': params.get('public_ip')
        }
        additional_properties = params.get('additional_properties')
        if additional_properties:
            payload.update(additional_properties)
        payload = check_payload(payload)
        logger.debug("Payload {0}".format(payload))
        response = il.make_rest_call(endpoint, 'POST', data=json.dumps(payload))
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def get_workloads(config, params):
    try:
        il = Illumio(config)
        endpoint = '/orgs/{0}/workloads'.format(params.get('org_id'))
        query_params = {
            'enforcement_mode': ENFORCEMENT_MODE.get(params.get('enforcement_mode')) if params.get(
                'enforcement_mode') else '',
            'include_deleted': params.get('include_deleted'),
            'security_policy_sync_state': params.get('security_policy_sync_state').lower() if params.get(
                'security_policy_sync_state') else '',
            'security_policy_update_mode': params.get('security_policy_update_mode').lower() if params.get(
                'security_policy_update_mode') else '',
            'visibility_level': VISIBILITY_LEVEL.get(params.get('visibility_level')) if params.get(
                'visibility_level') else '',
            'policy_health': params.get('policy_health').lower() if params.get('policy_health') else '',
            'max_results': params.get('max_results')
        }
        additional_fields = params.get('additional_fields')
        if additional_fields:
            query_params.update(additional_fields)
        query_params = {k: v for k, v in query_params.items() if v is not None and v != ''}
        logger.debug("Query Parameters {0}".format(query_params))
        response = il.make_rest_call(endpoint, 'GET', params=query_params)
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def get_workload_by_id(config, params):
    try:
        il = Illumio(config)
        endpoint = '/orgs/{0}/workloads/{1}'.format(params.get('org_id'), params.get('workload_id'))
        response = il.make_rest_call(endpoint, 'GET')
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def update_workload(config, params):
    try:
        cd = Illumio(config)
        endpoint = '/orgs/{0}/workloads/{1}'.format(params.get('org_id'), params.get('workload_id'))
        payload = {
            "name": params.get('name'),
            "description": params.get('description'),
            "service_provider": params.get('service_provider'),
            "enforcement_mode": ENFORCEMENT_MODE.get(params.get('enforcement_mode')) if params.get(
                'enforcement_mode') else ''
        }
        additional_properties = params.get('additional_properties')
        if additional_properties:
            payload.update(additional_properties)
        payload = check_payload(payload)
        logger.debug("Payload {0}".format(payload))
        response = cd.make_rest_call(endpoint, 'PUT', data=json.dumps(payload))
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def delete_workload(config, params):
    try:
        il = Illumio(config)
        endpoint = '/orgs/{0}/workloads/{1}'.format(params.get('org_id'), params.get('workload_id'))
        response = il.make_rest_call(endpoint, 'DELETE')
        return {"message": "Successfully deleted workload: {0}".format(params.get('workload_id'))}
    except Exception as err:
        raise ConnectorError(str(err))


def get_ransomware_details(config, params):
    try:
        il = Illumio(config)
        endpoint = '/orgs/{0}/workloads/{1}/risk_details'.format(params.get('org_id'), params.get('workload_id'))
        response = il.make_rest_call(endpoint, 'GET')
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def create_ip_list(config, params):
    try:
        il = Illumio(config)
        endpoint = '/orgs/{0}/sec_policy/{1}/ip_lists'.format(params.get('org_id'), params.get('pversion'))
        payload = {
            'name': params.get('name'),
            'description': params.get('description'),
            'ip_ranges': params.get('ip_ranges'),
            'fqdns': params.get('fqdns')
        }
        additional_properties = params.get('additional_properties')
        if additional_properties:
            payload.update(additional_properties)
        payload = check_payload(payload)
        logger.debug("Payload {0}".format(payload))
        response = il.make_rest_call(endpoint, 'POST', data=json.dumps(payload))
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def get_ip_list(config, params):
    try:
        il = Illumio(config)
        endpoint = '/orgs/{0}/sec_policy/{1}/ip_lists'.format(params.get('org_id'), params.get('pversion'))
        query_params = {
            'description': params.get('description'),
            'external_data_reference': params.get('external_data_reference'),
            'max_results': params.get('max_results')
        }
        additional_fields = params.get('additional_fields')
        if additional_fields:
            query_params.update(additional_fields)
        query_params = {k: v for k, v in query_params.items() if v is not None and v != ''}
        logger.debug("Query Parameters {0}".format(query_params))
        response = il.make_rest_call(endpoint, 'GET', params=query_params)
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def get_ip_list_by_id(config, params):
    try:
        il = Illumio(config)
        endpoint = '/orgs/{0}/sec_policy/{1}/ip_lists/{2}'.format(params.get('org_id'), params.get('pversion'),
                                                                  params.get('ip_list_id'))
        response = il.make_rest_call(endpoint, 'GET')
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def update_ip_list(config, params):
    try:
        il = Illumio(config)
        endpoint = '/orgs/{0}/sec_policy/{1}/ip_lists/{2}'.format(params.get('org_id'), params.get('pversion'),
                                                                  params.get('ip_list_id'))
        payload = {
            'description': params.get('description'),
            'ip_ranges': params.get('ip_ranges'),
            'fqdns': params.get('fqdns')
        }
        additional_properties = params.get('additional_properties')
        if additional_properties:
            payload.update(additional_properties)
        payload = check_payload(payload)
        logger.debug("Payload {0}".format(payload))
        response = il.make_rest_call(endpoint, 'PUT', data=json.dumps(payload))
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def delete_ip_list(config, params):
    try:
        il = Illumio(config)
        endpoint = '/orgs/{0}/sec_policy/{1}/ip_lists/{2}'.format(params.get('org_id'), params.get('pversion'),
                                                                  params.get('ip_list_id'))
        response = il.make_rest_call(endpoint, 'DELETE')
        return {"message": "Successfully deleted IP list: {0}".format(params.get('ip_list_id'))}
    except Exception as err:
        raise ConnectorError(str(err))


def create_label(config, params):
    try:
        il = Illumio(config)
        endpoint = '/orgs/{0}/labels'.format(params.get('org_id'))
        payload = {
            'key': params.get('key'),
            'value': params.get('value'),
            'external_data_set': params.get('external_data_set'),
            'external_data_reference': params.get('external_data_reference')
        }
        payload = check_payload(payload)
        logger.debug("Payload {0}".format(payload))
        response = il.make_rest_call(endpoint, 'POST', data=json.dumps(payload))
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def get_labels(config, params):
    try:
        il = Illumio(config)
        endpoint = '/orgs/{0}/labels'.format(params.get('org_id'))
        query_params = {
            'include_deleted': params.get('include_deleted'),
            'external_data_reference': params.get('external_data_reference'),
            'max_results': params.get('max_results')
        }
        additional_fields = params.get('additional_fields')
        if additional_fields:
            query_params.update(additional_fields)
        query_params = {k: v for k, v in query_params.items() if v is not None and v != ''}
        logger.debug("Query Parameters {0}".format(query_params))
        response = il.make_rest_call(endpoint, 'GET', params=query_params)
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def get_label_by_id(config, params):
    try:
        il = Illumio(config)
        endpoint = '/orgs/{0}/labels/{1}'.format(params.get('org_id'), params.get('label_id'))
        query_params = {
            'usage': params.get('usage')
        }
        query_params = {k: v for k, v in query_params.items() if v is not None and v != ''}
        logger.debug("Query Parameters {0}".format(query_params))
        response = il.make_rest_call(endpoint, 'GET', params=query_params)
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def update_label(config, params):
    try:
        il = Illumio(config)
        endpoint = '/orgs/{0}/labels/{1}'.format(params.get('org_id'), params.get('label_id'))
        payload = {
            'value': params.get('value'),
            'external_data_set': params.get('external_data_set'),
            'external_data_reference': params.get('external_data_reference')
        }
        payload = check_payload(payload)
        logger.debug("Payload {0}".format(payload))
        response = il.make_rest_call(endpoint, 'PUT', data=json.dumps(payload))
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def delete_label(config, params):
    try:
        il = Illumio(config)
        endpoint = '/orgs/{0}/labels/{1}'.format(params.get('org_id'), params.get('label_id'))
        response = il.make_rest_call(endpoint, 'DELETE')
        return {"message": "Successfully deleted label: {0}".format(params.get('label_id'))}
    except Exception as err:
        raise ConnectorError(str(err))


def get_pending_security_policy(config, params):
    try:
        il = Illumio(config)
        endpoint = '/orgs/{0}/sec_policy/pending'.format(params.get('org_id'))
        query_params = {
            'max_results': params.get('max_results')
        }
        query_params = {k: v for k, v in query_params.items() if v is not None and v != ''}
        logger.debug("Query Parameters {0}".format(query_params))
        response = il.make_rest_call(endpoint, 'GET', params=query_params)
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def revert_pending_uncommitted_security_policy_list(config, params):
    try:
        il = Illumio(config)
        endpoint = '/orgs/{0}/sec_policy/pending'.format(params.get('org_id'))
        response = il.make_rest_call(endpoint, 'DELETE')
        return {"message": "Successfully reverted pending uncommitted security policy"}
    except Exception as err:
        raise ConnectorError(str(err))


def restore_previous_security_policy(config, params):
    try:
        il = Illumio(config)
        payload = {}
        endpoint = '/orgs/{0}/sec_policy/{1}/restore'.format(params.get('org_id'), params.get('pversion'))
        response = il.make_rest_call(endpoint, 'POST', data=json.dumps(payload))
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def send_custom_request(config, params):
    try:
        il = Illumio(config)
        endpoint = params.get("endpoint")
        http_method = params.get("method")
        if params.get("query_params"):
            query_params = params.get("query_params")
        else:
            query_params = None
        if params.get("payload"):
            payload = params.get("payload")
        else:
            payload = None
        response = il.make_rest_call(endpoint, method=http_method, params=query_params, data=json.dumps(payload))
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def _health(config, params):
    try:
        il = Illumio(config)
        endpoint = '/health'
        response = il.make_rest_call(endpoint, 'GET')
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def check_health(config):
    try:
        response = _health(config, params={})
        if response:
            return True
    except Exception as err:
        logger.info(str(err))
        raise ConnectorError(str(err))


operations = {
    'create_workload': create_workload,
    'get_workloads': get_workloads,
    'get_workload_by_id': get_workload_by_id,
    'update_workload': update_workload,
    'delete_workload': delete_workload,
    'get_ransomware_details': get_ransomware_details,
    'create_ip_list': create_ip_list,
    'get_ip_list': get_ip_list,
    'get_ip_list_by_id': get_ip_list_by_id,
    'update_ip_list': update_ip_list,
    'delete_ip_list': delete_ip_list,
    'create_label': create_label,
    'get_labels': get_labels,
    'get_label_by_id': get_label_by_id,
    'update_label': update_label,
    'delete_label': delete_label,
    'get_pending_security_policy': get_pending_security_policy,
    'revert_pending_uncommitted_security_policy_list': revert_pending_uncommitted_security_policy_list,
    'restore_previous_security_policy': restore_previous_security_policy,
    'send_custom_request': send_custom_request
}
