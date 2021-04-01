#!/usr/bin/python3

# import the requests library
import requests
import sys
import json

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# create a main() method
def getVRF(HOST, USER, PASS):
    #HOST = '1.1.1.1'
    #USER = 'user'
    #PASS = 'password'

    # url string to issue GET request
    #url = "https://{h}/restconf/data/ietf-interfaces:interfaces".format(h=HOST)
    url = f"https://{HOST}/restconf/data/Cisco-IOS-XE-vrf-oper:vrf-oper-data"

    # RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}
    # this statement performs a GET on the specified url
    response = requests.get(url, auth=(USER, PASS),
                            headers=headers, verify=False)
    json_data = json.loads(response.text)
    # return the json from response
    return(json_data)

if __name__ == '__main__':
    sys.exit(getVRF('1.1.1.1', 'user', 'password'))
