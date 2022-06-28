from ncclient import manager

with manager.connect(host="192.168.1.211", port=830, username="OEUser01", hostkey_verify=False) as m:
    c = m.get_config(source='running').data_xml
    with open("%s.xml" % host, 'w') as f:
        f.write(c)