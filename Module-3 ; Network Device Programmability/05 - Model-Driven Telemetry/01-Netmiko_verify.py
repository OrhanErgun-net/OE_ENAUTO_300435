from netmiko import ConnectHandler

R1 = {'device_type': 'cisco_ios',
    'ip': '192.168.1.211',
    'username': 'OEUSer01',
    'password': 'oe123123enauto'}

net_connect = ConnectHandler(**R1)

output = net_connect.send_command("show run | sec tel")
net_connect.disconnect()

print (output)