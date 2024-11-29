## About the connector
Illumio that provides a platform designed to help organizations protect their critical applications and data by creating secure zones and controlling access between workloads, regardless of whether those workloads are on-premises or in the cloud. This connector facilitates automated operations related to workloads, IP list and labels.
<p>This document provides information about the Illumio Core Connector, which facilitates automated interactions, with a Illumio Core server using FortiSOAR&trade; playbooks. Add the Illumio Core Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Illumio Core.</p>

### Version information

Connector Version: 1.0.0

Authored By: Fortinet

Certified: No

## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-illumio-core</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Illumio Core server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Illumio Core server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Illumio Core</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the URL of the Illumio server to connect and perform automated operations.
</td>
</tr><tr><td>API Key</td><td>Specify the API Key to access the endpoint to connect and perform the automated operations
</td>
</tr><tr><td>API Token</td><td>Specify the API Token to access the endpoint to connect and perform the automated operations
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Create Workload</td><td>Creates an workload in Illumio based on the organization ID, workload name, and other input parameters that you have specified.</td><td>create_workload <br/>Investigation</td></tr>
<tr><td>Get Workloads</td><td>Retrieve a list of workloads from Illumio based on the organization ID and other input parameters you have specified.</td><td>get_workloads <br/>Investigation</td></tr>
<tr><td>Get Workload by ID</td><td>Retrieves a specific workload from Illumio based on the organization ID and workload ID that you have specified.</td><td>get_workload_by_id <br/>Investigation</td></tr>
<tr><td>Update Workload</td><td>Updates an workload in Illumio based on the organization ID, workload ID, and other input parameters that you have specified.</td><td>update_workload <br/>Investigation</td></tr>
<tr><td>Delete Workload</td><td>Delete an workload in Illumio based on the organization ID and workload ID that you have specified.</td><td>delete_workload <br/>Investigation</td></tr>
<tr><td>Get Ransomware Details</td><td>Retrieve a specific ransomware details for the workload from Illumio based on the organization ID and workload ID that you have specified.</td><td>get_ransomware_details <br/>Investigation</td></tr>
<tr><td>Create IP List</td><td>Creates an IP list in Illumio based on the organization ID, security policy version, IP list name, and other input parameters you have specified.</td><td>create_ip_list <br/>Investigation</td></tr>
<tr><td>Get IP List</td><td>Retrieve a IP list from Illumio based on the organization ID, security policy version, and other input parameters you have specified.</td><td>get_ip_list <br/>Investigation</td></tr>
<tr><td>Get IP List by ID</td><td>Retrieve a specific IP list details from Illumio based on the organization ID, security policy version, and IP list ID that you have specified.</td><td>get_ip_list_by_id <br/>Investigation</td></tr>
<tr><td>Update IP List</td><td>Updates an IP list in Illumio based on the organization ID, security policy version, IP list ID, and other input parameters you have specified.</td><td>update_ip_list <br/>Investigation</td></tr>
<tr><td>Delete IP List</td><td>Delete an IP list in Illumio based on the organization ID, security policy version, and IP list ID that you have specified.</td><td>delete_ip_list <br/>Investigation</td></tr>
<tr><td>Create Label</td><td>Creates an label in Illumio based on the organization ID, and other input parameters you have specified.</td><td>create_label <br/>Investigation</td></tr>
<tr><td>Get Labels</td><td>Retrieve a labels from Illumio based on the organization ID, and other input parameters you have specified.</td><td>get_labels <br/>Investigation</td></tr>
<tr><td>Get Label by ID</td><td>Retrieve a specific label details from Illumio based on the organization ID, label ID, and other input parameter that you have specified.</td><td>get_label_by_id <br/>Investigation</td></tr>
<tr><td>Update Label</td><td>Updates an label in Illumio based on the organization ID, label ID, and other input parameters you have specified.</td><td>update_label <br/>Investigation</td></tr>
<tr><td>Delete Label</td><td>Delete an label in Illumio based on the organization ID and label ID that you have specified.</td><td>delete_label <br/>Investigation</td></tr>
<tr><td>Get Pending Security Policy</td><td>Retrieve a pending security policy from Illumio based on the organization ID, and other input parameter that you have specified.</td><td>get_pending_security_policy <br/>Investigation</td></tr>
<tr><td>Revert Pending Uncommitted Security Policy List</td><td>Revert the collection of pending uncommitted security policy objects in Illumio based on the organization ID you have specified.</td><td>revert_pending_uncommitted_security_policy_list <br/>Investigation</td></tr>
<tr><td>Restore Previous Security Policy</td><td>Restore previous security policy in Illumio based on the organization ID and security policy version you have specified.</td><td>restore_previous_security_policy <br/>Investigation</td></tr>
<tr><td>Execute an API Call</td><td>Sends an API request to any API endpoint based on specified HTTP method, endpoint, and other input parameters that you have specified, enabling flexible API interactions tailored to user needs. </td><td>send_custom_request <br/>Investigation</td></tr>
</tbody></table>

### operation: Create Workload
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the ID of the organization based on which you want to create workload in Illumio.
</td></tr><tr><td>Workload Name</td><td>Specify the name of the workload to create in Illumio.
</td></tr><tr><td>Description</td><td>Specify the description of the workload to create in Illumio.
</td></tr><tr><td>Hostname</td><td>Specify the hostname of the workload to create in Illumio.
</td></tr><tr><td>Service Principal Name</td><td>Specify the principal name of the service based on which you want to create workload in Illumio.
</td></tr><tr><td>Public IP</td><td>Specify the public IP based on which you want to create workload in Illumio.
</td></tr><tr><td>Additional Properties</td><td>Additional fields, in the JSON format, based on which you want to create workload in Illumio.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Get Workloads
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the ID of the organization based on which you want to retrieve workloads from Illumio.
</td></tr><tr><td>Enforcement Mode</td><td>Select a enforcement mode of the workload based on which you want to retrieve workloads from Illumio. You can choose from the following options: Visibility Only, Full, Idle, or Selective.
</td></tr><tr><td>Included Deleted</td><td>Select the option, if you want to include deleted workloads in the records from Illumio.
</td></tr><tr><td>Security Policy Sync State</td><td>Select a security policy sync state of the workload based on which you want to retrieve workloads from Illumio. You can select the option as Staged.
</td></tr><tr><td>Security Policy Update Mode</td><td>Select a security policy update mode of the workload based on which you want to retrieve workloads from Illumio. You can choose from the following options: Static or Adaptive.
</td></tr><tr><td>Visibility Level</td><td>Select a visibility level of the workload based on which you want to retrieve workloads from Illumio. You can choose from the following options: Flow Full Detail, Flow Summary, Flow Drops, Flow Off, or Enhanced Data Collection.
</td></tr><tr><td>Policy Health</td><td>Select a policy health of the workload based on which you want to retrieve workloads from Illumio. You can choose from the following options: Active, Warning, Error, or Suspended.
</td></tr><tr><td>Limit</td><td>Maximum number of workload that this operation should return from Illumio.
</td></tr><tr><td>Additional Properties</td><td>Additional fields, in the JSON format, based on which you want to retrieve details from Illumio.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Get Workload by ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the ID of the organization based on which you want to retrieve workload from Illumio.
</td></tr><tr><td>Workload ID</td><td>Specify the ID of the workload to retrieve its details from Illumio.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Update Workload
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the ID of the organization based on which you want to update workload in Illumio.
</td></tr><tr><td>Workload ID</td><td>Specify the ID of the workload which you want to update in Illumio.
</td></tr><tr><td>Workload Name</td><td>Specify the name of the workload which you want to update in Illumio.
</td></tr><tr><td>Description</td><td>Specify the description of the workload which you want to update in Illumio.
</td></tr><tr><td>Service Provider</td><td>Specify the service provider of the workload which you want to update in Illumio.
</td></tr><tr><td>Enforcement Mode</td><td>Select a enforcement mode of the workload based on which you want to update workload in Illumio. You can choose from the following options: Visibility Only, Full, Idle, or Selective.
</td></tr><tr><td>Additional Properties</td><td>Additional fields, in the JSON format, based on which you want to update workload in Illumio.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Delete Workload
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the ID of the organization based on which you want to delete workload in Illumio.
</td></tr><tr><td>Workload ID</td><td>Specify the ID of the workload which you want to delete in Illumio.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Get Ransomware Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the ID of the organization based on which you want to retrieve ransomware details from Illumio.
</td></tr><tr><td>Workload ID</td><td>Specify the ID of the workload based on which you want to retrieve ransomware details from Illumio.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Create IP List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the ID of the organization based on which you want to create IP list in Illumio.
</td></tr><tr><td>Security Policy Version</td><td>Specify the security policy version based on which you want to create IP list in Illumio.
</td></tr><tr><td>IP List Name</td><td>Specify the name of the IP list based on which you want to create IP list in Illumio.
</td></tr><tr><td>IP Ranges</td><td>Specify the IP addresses or ranges, in the JSON format, based on which you want to create IP list in Illumio.
</td></tr><tr><td>Fully Qualified Domain Name (FQDN)</td><td>Specify the fully qualified domain name (FQDN), in the JSON format, based on which you want to create IP list in Illumio.
</td></tr><tr><td>Description</td><td>Specify the description based on which you want to create IP list in Illumio.
</td></tr><tr><td>Additional Properties</td><td>Additional fields, in the JSON format, based on which you want to create IP list in Illumio.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Get IP List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the ID of the organization based on which you want to retrieve IP list from Illumio.
</td></tr><tr><td>Security Policy Version</td><td>Specify the security policy version based on which you want to retrieve IP list from Illumio.
</td></tr><tr><td>Description</td><td>Specify the description based on which you want to retrieve IP list from Illumio.
</td></tr><tr><td>External Data Reference</td><td>Specify a unique identifier within the external data source based on which you want to retrieve IP list from Illumio.
</td></tr><tr><td>Limit</td><td>Maximum number of IP list that this operation should return from Illumio.
</td></tr><tr><td>Additional Properties</td><td>Additional fields, in the JSON format, based on which you want to retrieve details from Illumio.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Get IP List by ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the ID of the organization based on which you want to retrieve IP list details from Illumio.
</td></tr><tr><td>Security Policy Version</td><td>Specify the security policy version based on which you want to retrieve IP list details from Illumio.
</td></tr><tr><td>IP List ID</td><td>Specify the ID of the IP list based on which you want to retrieve details from Illumio.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Update IP List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the ID of the organization based on which you want to update IP list in Illumio.
</td></tr><tr><td>Security Policy Version</td><td>Specify the security policy version based on which you want to update IP list in Illumio.
</td></tr><tr><td>IP List ID</td><td>Specify the ID of the IP list which you want to update details in Illumio.
</td></tr><tr><td>IP Ranges</td><td>Specify the IP addresses or ranges, in the JSON format, based on which you want to update IP list in Illumio.
</td></tr><tr><td>Fully Qualified Domain Name (FQDN)</td><td>Specify the fully qualified domain name (FQDN), in the JSON format, based on which you want to update IP list in Illumio.
</td></tr><tr><td>Description</td><td>Specify the description based on which you want to update IP list in Illumio.
</td></tr><tr><td>Additional Properties</td><td>Additional fields, in the JSON format, based on which you want to update details in Illumio.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Delete IP List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the ID of the organization based on which you want to delete IP list in Illumio.
</td></tr><tr><td>Security Policy Version</td><td>Specify the security policy version based on which you want to delete IP list in Illumio.
</td></tr><tr><td>IP List ID</td><td>Specify the ID of the IP list which you want to delete in Illumio.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Create Label
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the ID of the organization based on which you want to create label in Illumio.
</td></tr><tr><td>Label Key</td><td>Specify the label key based on which you want to create label in Illumio.
</td></tr><tr><td>Label Value</td><td>Specify the label value based on which you want to create label in Illumio.
</td></tr><tr><td>External Data Set</td><td>Specify the external data set identifier based on which you want to create label in Illumio.
</td></tr><tr><td>External Data Reference</td><td>Specify the external data reference identifier based on which you want to create label in Illumio.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Get Labels
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the ID of the organization based on which you want to retrieve labels from Illumio.
</td></tr><tr><td>Include Deleted</td><td>Select the option, if you want to include deleted labels in the records from Illumio.
</td></tr><tr><td>External Data Reference</td><td>Specify a unique identifier within the external data source based on which you want to retrieve labels from Illumio.
</td></tr><tr><td>Limit</td><td>Maximum number of labels that this operation should return from Illumio.
</td></tr><tr><td>Additional Properties</td><td>Additional fields, in the JSON format, based on which you want to retrieve labels from Illumio.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Get Label by ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the ID of the organization based on which you want to retrieve label details from Illumio.
</td></tr><tr><td>Label ID</td><td>Specify the ID of the label based on which you want to retrieve details from Illumio.
</td></tr><tr><td>Include Label Usage Flag</td><td>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Update Label
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the ID of the organization based on which you want to update label in Illumio.
</td></tr><tr><td>Label ID</td><td>Specify the ID of the label which you want to update details in Illumio.
</td></tr><tr><td>Label Value</td><td>Specify the label value based on which you want to update label in Illumio.
</td></tr><tr><td>External Data Set</td><td>Specify the external data set identifier based on which you want to update label in Illumio.
</td></tr><tr><td>External Data Reference</td><td>Specify the external data reference identifier based on which you want to update label in Illumio.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Delete Label
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the ID of the organization based on which you want to delete label in Illumio.
</td></tr><tr><td>Label ID</td><td>Specify the ID of the label which you want to delete in Illumio.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Get Pending Security Policy
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the ID of the organization based on which you want to retrieve pending security policy from Illumio.
</td></tr><tr><td>Limit</td><td>Maximum number of pending security policy that this operation should return from Illumio.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Revert Pending Uncommitted Security Policy List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the ID of the organization based on which you want to revert pending uncommitted security policy in Illumio.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Restore Previous Security Policy
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the ID of the organization based on which you want to restore previous security policy in Illumio.
</td></tr><tr><td>Security Policy Version</td><td>Specify the security policy version based on which you want to restore previous security policy in Illumio.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Execute an API Call
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>HTTP Method</td><td>Select an HTTP action for the request. You can select from the following options:  

DELETE 

GET 

PATCH 

POST 

PUT 
</td></tr><tr><td>Endpoint</td><td>Specify the target API URL path for the request. 
For example, if the website is "https://example.com " and URL path is "/images/pic.jpg". The endpoint would be "/images/pic.jpg". 
</td></tr><tr><td>Query Parameters</td><td>(Optional) Specify any optional parameters to add to the URL and refine the request. 
</td></tr><tr><td>Request Payload</td><td>(Optional) Specify data, as JSON, to be sent as the request payload (typically for POST or PUT requests). 
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
## Included playbooks
The `Sample - Illumio Core - 1.0.0` playbook collection comes bundled with the Illumio Core connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Illumio Core connector.

- Create IP List
- Create Label
- Create Workload
- Delete IP List
- Delete Label
- Delete Workload
- Execute an API Call
- Get IP List
- Get IP List by ID
- Get Label by ID
- Get Labels
- Get Pending Security Policy
- Get Ransomware Details
- Get Workload by ID
- Get Workloads
- Restore Previous Security Policy
- Revert Pending Uncommitted Security Policy List
- Update IP List
- Update Label
- Update Workload

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
