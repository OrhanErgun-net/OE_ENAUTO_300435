from netmiko import ConnectHandler

cisco_csr1000 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.1.211',
    'username': 'OEUser01',
    'password': 'oe123123enauto',
    'port' : 22,
    'secret': '',
}

net_connect = ConnectHandler(**cisco_csr1000)

output = net_connect.send_command('show ip int brief')
print(output)