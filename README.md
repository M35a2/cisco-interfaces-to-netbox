# cisco-interfaces-to-netbox
Takes interfaces in a switch or router and adds the IP address to netbox
it loops through a csv list of devices and pulls the vrf information and ip information
then adds the prefix and IP's to netbox

If you need help with this, or run into an issue, let me know. I would be glad to help. 
This code is not production ready. Tested only on IOS-XE code in a lab.

# install modules
- install requests module
- install netbox python module
- install netaddr

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
   ![multi-vrf example](https://github.com/M35a2/cisco-interfaces-to-netbox/blob/main/screenshots/multivrf%20example.PNG)

to execute:
python3 run.py

![sample run.py](https://github.com/M35a2/cisco-interfaces-to-netbox/blob/main/screenshots/runpy-sample.PNG)
![sample netbox prefixes 1](https://github.com/M35a2/cisco-interfaces-to-netbox/blob/main/screenshots/prefixes1.PNG)
![sample netbox prefixes 2](https://github.com/M35a2/cisco-interfaces-to-netbox/blob/main/screenshots/prefixes2.PNG)
![sample netbox ip addresses 1](https://github.com/M35a2/cisco-interfaces-to-netbox/blob/main/screenshots/ip%20address1.PNG)
![sample netbox ip addresses 2](https://github.com/M35a2/cisco-interfaces-to-netbox/blob/main/screenshots/ip%20address2.PNG)
