import xmltodict
from lxml.etree import fromstring
from ncclient import manager

m = manager.connect(host='192.168.1.211', port=830, username='OEUser01',
                    password='oe123123enauto', device_params={'name': 'csr'})

Xpath = "/process-cpu-ios-xe-oper:cpu-usage/cpu-utilization/five-seconds"
RPC = f'''
    <establish-subscription xmlns='urn:ietf:params:xml:ns:yang:ietf-event-notifications' xmlns:yp='urn:ietf:params:xml:ns:yang:ietf-yang-push'>
        <stream>yp:yang-push</stream>
        <yp:xpath-filter>{Xpath}</yp:xpath-filter>
        <yp:period>500</yp:period>
    </establish-subscription>
'''

RPC_Res = m.dispatch(fromstring(RPC))

while True:

    T_Notification = xmltodict.parse(m.take_notification().notification_xml)

    print(f" {T_Notification['notification']['push-update']['datastore-contents-xml']['cpu-usage']['cpu-utilization']['five-seconds']}% CPU")
    