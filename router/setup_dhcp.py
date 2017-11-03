import random

mac_ip_table = {}


def get_ip_for_host_machine(mac_ip, network_prefix):
    if mac_ip in mac_ip_table.keys():
        return mac_ip_table[mac_ip]
    else:
        host_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(2))))
        network_address = network_prefix.split('.')
        final_ip = network_address[1] + '.' + network_address[2]+'.' + host_ip
        if final_ip not in mac_ip_table.values():
            mac_ip_table[mac_ip] = final_ip

    return final_ip
