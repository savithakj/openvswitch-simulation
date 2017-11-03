from uuid import getnode as get_mac

import re, uuid
from router import setup_dhcp

def main():
    mac_id = get_mac_id()
    network_address = get_router_address()
    ovs_address = get_ovs_adress()
    ip_address=setup_dhcp.get_ip_for_host_machine(mac_id,network_address)
    print("IP Address : "+ip_address)


def get_mac_id():
    mac_id = ':'.join(re.findall('..', '%012x' % get_mac()))
    print(" Physical Address : ", mac_id)

    return mac_id


def get_router_address():
    network_address = input("Network Connected to : ")
    return network_address


def get_ovs_adress():
    ovs_address = input("OVS Connected to : ")
    return ovs_address


if __name__ == '__main__':
    main()
