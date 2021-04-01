from netbox import NetBox
import requests
import json
import csv
from re import search
requests.packages.urllib3.disable_warnings()

def createAddress(address, description, vrf, network, role):
    
    #netbox settings
    netbox = NetBox(host='10.255.X.X', port=443, use_ssl=True, auth_token='5d6dfe9f6f39785eb86f')    

    # set VRF ID
    id = 0
    #attempt to create prefix if its not already there
    if vrf == "GRT":
        id = 1
        try:
            netboxPrefix = netbox.ipam.create_ip_prefix(prefix = network, vrf = id)
        except:
            print("prefix already exists")   
    elif not vrf:
        try:
            netboxPrefix = netbox.ipam.create_ip_prefix(prefix = network)
        except:
            print("prefix already exists")

    #set VRF ID
    id2 = 0
    #attempt to create address
    if vrf == "GRT":
        id2 = 1
        loopback = "Loopback"
        if search(loopback, role):
            try:    
                netboxAPIcall = netbox.ipam.create_ip_address(address = address, vrf = id2, description = description, role = "10")
            except:
                print("ip address already exists")
        else:
            try:    
                netboxAPIcall = netbox.ipam.create_ip_address(address = address, vrf = id2, description = description)
            except:
                print("ip address already exists")
    elif vrf == "":
        loopback = "Loopback"
        if search(loopback, role):
            try:    
                netboxAPIcall = netbox.ipam.create_ip_address(address = address, description = description, role = "10")
            except:
                print("ip address already exists")
        else:
            try:    
                netboxAPIcall = netbox.ipam.create_ip_address(address = address, description = description)
            except:
                print("ip address already exists")






