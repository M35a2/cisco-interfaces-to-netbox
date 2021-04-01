# cisco-interfaces-to-netbox
Takes interfaces in a switch or router and adds the IP address to netbox
it loops through a csv list of devices and pulls the vrf information and ip information
then adds the 
Tested only on IOS-XE code

# install modules
install requests module
install netbox python module
install netaddr

# setup variables
-edit the hosts.csv for your devices
  example: hostname,ip,user,password

-in pushnetbox.py change the host ip and auth_token

-If interfaces use a VRF, the VRF needs prebuilt in netbox. 
  Then set the vrf ID in the pushnetbox.py
  if you only have 1 vrf created in netbox, the ID will be "1"
  change line 16 and 31 of pushnetbox.py to equal the vrf name. 
  eg: if vrf == "MYvrf":
  if you have multiple vrf's, copy/paste the two if statements for the vrf's and set the proper ID
  eg: 
    id = 0
    //attempt to create prefix if its not already there
    if vrf == "GRT":
        id = 1
        try:
            netboxPrefix = netbox.ipam.create_ip_prefix(prefix = network, vrf = id)
        except:
            print("prefix already exists")   
    //NEW VRF    
    elif vrf == "MYvrf":
        id = 2
        try:
            netboxPrefix = netbox.ipam.create_ip_prefix(prefix = network, vrf = id)
        except:
            print("prefix already exists")           
    elif not vrf:
        try:
            netboxPrefix = netbox.ipam.create_ip_prefix(prefix = network)
        except:
            print("prefix already exists")

   //set VRF ID
    id2 = 0
    //attempt to create address
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
    //NEW VRF     
    elif vrf == "MYvrf":
        id2 = 2
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

to execute:
python3 run.py

![sample run.py](https://github.com/M35a2/cisco-interfaces-to-netbox/blob/main/screenshots/runpy-sample.PNG)
![sample netbox prefixes 1](https://github.com/M35a2/cisco-interfaces-to-netbox/blob/main/screenshots/prefixes1.PNG)
![sample netbox prefixes 2](https://github.com/M35a2/cisco-interfaces-to-netbox/blob/main/screenshots/prefixes2.PNG)
![sample netbox ip addresses 1](https://github.com/M35a2/cisco-interfaces-to-netbox/blob/main/screenshots/ip%20address1.PNG)
![sample netbox ip addresses 2](https://github.com/M35a2/cisco-interfaces-to-netbox/blob/main/screenshots/ip%20address2.PNG)
