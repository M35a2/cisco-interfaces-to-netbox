from netaddr import IPAddress
from netaddr import IPNetwork

# return cidr for a given subnet mask
def netmaskToCidr(netmask):
    return(IPAddress(netmask).netmask_bits())

# return network address to an ip address
def networkID(IP):
    ip = IPNetwork(IP)
    return(ip.network)
