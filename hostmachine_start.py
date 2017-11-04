from uuid import getnode as get_mac
from router.setup_dhcp import get_ip_for_host_machine
import re, uuid


class HostMachine:
    def start(self):
        mac_id = self.get_mac_id()
        network_address = self.get_router_address()
        # TODO check if router is started

        ovs_address = self.get_ovs_adress()
        #TODO check if the OVS is up
        ip_address = get_ip_for_host_machine(mac_id, network_address)
        print("IP Address : " + ip_address)

    def get_mac_id(self):
        mac_id = ':'.join(re.findall('..', '%012x' % get_mac()))
        print(" Physical Address : ", mac_id)

        return mac_id

    def get_router_address(self):
        network_address = input("Network Connected to : ")
        return network_address

    def get_ovs_adress(self):
        ovs_address = input("OVS Connected to : ")
        return ovs_address


if __name__ == '__main__':
    hostmachine = HostMachine()
    hostmachine.start()
