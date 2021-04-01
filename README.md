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
edit the hosts.csv for your devices
example: hostname,ip,user,password

in pushnetbox.py change the host ip and auth_token

to execute:
python3 run.py

