from netmiko import ConnectHandler

with open ("SubscribeRouter.txt",'r') as f:
    Configs = f.readlines()
print (Configs)

R1 = {'device_type': 'cisco_ios',
    'ip': '192.168.1.211',
    'username': 'OEUSer01',
    'password': 'oe123123enauto'}

net_connect = ConnectHandler(**R1)

output = net_connect.send_config_set(Configs)
net_connect.disconnect()

print (output)