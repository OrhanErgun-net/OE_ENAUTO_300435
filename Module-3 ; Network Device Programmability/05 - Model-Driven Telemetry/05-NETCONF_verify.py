import xmltodict
import xml.dom.minidom
from lxml.etree import fromstring
from ncclient import manager

m = manager.connect(host='192.168.1.211', port=830, username='OEUser01',
                    password='oe123123enauto', device_params={'name': 'csr'})

Filter_X="/mdt-oper-data/mdt-subscriptions"
netconf_reply = m.get(filter=("xpath",Filter_X))

XD = xml.dom.minidom.parseString( str(netconf_reply))
print(XD.toprettyxml( indent = "  " ))