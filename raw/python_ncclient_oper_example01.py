from ncclient import manager

DeviceInfo = {
    "host": "192.168.1.211",
    "port": "830",
    "username": "OEUser01",
    "password": "oe123123enauto"
}

xml_message = """
<filter>
   <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"> 
        <interface>
            <name>GigabitEthernet1</name>
        </interface>
    </interfaces>
    <interface-state xmlns="urn:ietf:params:xml:ns:ietf-interfaces">
        <interface>
            <name>GigabitEthernet1</name>
        </interface>
    </interfaces-state>
</filter>
"""

with manager.connect(**DeviceInfo, hostkey_verify=False) as m:
    netconf_response = m.get(xml_message)
