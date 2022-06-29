from ncclient import manager

RouterR1 =  manager.connect(host="192.168.1.211",
                    port=830,
                    username="OEUser01",
                    password="oe123123enauto",
                    hostkey_verify=False,
                    device_params={'name':'csr'})

FILTER = '''
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native
        xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface><GigabitEthernet><name>1</name></GigabitEthernet></interface>
    </native>
</filter>
'''

print (RouterR1.get_config("running", FILTER))
RouterR1.close_session()