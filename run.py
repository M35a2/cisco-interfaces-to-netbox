import json
import csv
import requests
from re import search
from requests.auth import HTTPBasicAuth
from getvrf import getVRF
from getinterfaces import getInterfaces
from netaddress import netmaskToCidr
from netaddress import networkID
from pushnetbox import createAddress
requests.packages.urllib3.disable_warnings()

#open the CSV file which contains name,ip,un,pw
with open('hosts.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            #get vrf data from device
            vrfData = getVRF(row[1], row[2], row[3])
            #get interface data from device
            interfacesData = getInterfaces(row[1], row[2], row[3])
            #for each interface pulled from the device
            for interfaces in (interfacesData['ietf-interfaces:interfaces']['interface']):
                #set interface name
                interfaceName = (interfaces['name'])
                try:
                    # get the interface from the json data
                    interfaceIp = (interfaces['ietf-ip:ipv4']['address'][0]['ip'])
                    #get the subnet from the json data
                    interfaceSubnet = (interfaces['ietf-ip:ipv4']['address'][0]['netmask'])
                    #set the cidr from subnet
                    cidr = netmaskToCidr(interfaceSubnet)
                    a = f'/{cidr}'
                    #create blank string for vrf
                    vrf = ''
                    # if the interface is in a vrf, set the vrf name
                    if interfaceName in (vrfData['Cisco-IOS-XE-vrf-oper:vrf-oper-data']['vrf-entry'][0]['interface']):
                       vrf = vrfData['Cisco-IOS-XE-vrf-oper:vrf-oper-data']['vrf-entry'][0]['vrf-name']
                    #build the interface ip '1.1.1.1/32'
                    IP = (f'{interfaceIp}{a}')
                    #build the description for the interface
                    description = (f'{row[0]} int {interfaceName}')
                    #obtain the network id based on subnet from netaddress.py
                    network = networkID(IP)
                    network = f'{network}{a}'
                    # build the role
                    lo = "Loopback"
                    role = ''
                    # if there is Loopback in the interface name, set role to 'loopback'
                    if search(lo, interfaceName):
                        role = "Loopback"
                    #print output gathered from json data
                    print(f" adding: address = '{IP}', vrf = '{vrf}', description = '{description}', role = '{role}')")    
                    #attempt to add to create the address from pushnetbox.py
                    try:
                        netboxAPIcall = createAddress(IP, description, vrf, network, role)
                    except Exception as e:
                        print(f'error creating reservation for {interfaceName}')
                        print(e)

                # if the interface does not have an ip address, the above will fail and print this output, then continue to loop
                except Exception as e:
                    print(f'{row[0]} int {interfaceName} does not have an ip address')
                    print(f'error: {e}')
print("*" * 20)
