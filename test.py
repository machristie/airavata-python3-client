
from apache.airavata.api import Airavata
from apache.airavata.api.ttypes import *
from apache.airavata.model.workspace.ttypes import *
from apache.airavata.model.security.ttypes import AuthzToken

import requests

from thrift import Thrift
from thrift.transport import TSSLSocket
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import configparser

def get_transport(hostname, port):
    # Create a socket to the Airavata Server
    # TODO: validate server certificate
    transport = TSSLSocket.TSSLSocket(hostname, port, validate=False)

    # Use Buffered Protocol to speedup over raw sockets
    transport = TTransport.TBufferedTransport(transport)
    return transport

def get_airavata_client(transport):
    # Airavata currently uses Binary Protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a Airavata client to use the protocol encoder
    airavataClient = Airavata.Client(protocol)
    return airavataClient

def get_authz_token(accessTokenURL, userInfoURL, clientKey, clientSecret, username, password, gatewayID):
    
    request_data = {'grant_type': 'password', 'scope': 'openid', 'username': username, 'password': password}
    access_token_req = requests.post(accessTokenURL, auth=(clientKey, clientSecret), data=request_data, verify=False)
    access_token = access_token_req.json()['access_token']
    user_info_req = requests.get(userInfoURL, headers={'Authorization': "Bearer " + access_token}, verify=False)
    
    return AuthzToken(accessToken=access_token, claimsMap={'gatewayID': gatewayID, 'userName': user_info_req.json()['sub']})

def get_all_projects(airavataClient, authzToken, gatewayId, username):

    projectLists = airavataClient.getUserProjects(authzToken, gatewayId, username, -1, 0)

    return projectLists

if __name__ == '__main__':
    
    config = configparser.ConfigParser()
    config.read('airavata-client.ini')
    accessTokenURL = config['identity-server']['AccessTokenURL']
    userInfoURL = config['identity-server']['UserInfoURL']
    clientKey = config['identity-server']['ClientKey']
    clientSecret = config['identity-server']['ClientSecret']
    tenantDomain = config['identity-server']['TenantDomain']
    
    username = config['credentials']['Username']
    password = config['credentials']['Password']
    gatewayID = config['credentials']['GatewayID']
    authz_token = get_authz_token(accessTokenURL, userInfoURL, clientKey, clientSecret, username + "@" + tenantDomain, password, gatewayID)
    print(authz_token)
    
    hostname = config['airavata-api-server']['Hostname']
    port = config['airavata-api-server']['Port']
    transport = get_transport(hostname, port)
    transport.open()
    airavataClient = get_airavata_client(transport)
    
    projects = get_all_projects(airavataClient, authz_token, gatewayID, username)
    transport.close()
    print(projects)
