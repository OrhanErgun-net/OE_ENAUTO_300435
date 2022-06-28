from ncclient import manager

RouterR1 =  manager.connect(host="192.168.1.211",
                    port=830,
                    username="OEUser01",
                    password="oe123123enauto",
                    hostkey_verify=False,
                    device_params={'name':'csr'})

CONFIGURE = '''
<config>
    <native
        xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>R1byNETCONF</hostname>
    </native>
</config>
'''

print (RouterR1.get_config("running", CONFIGURE))
RouterR1.close_session()