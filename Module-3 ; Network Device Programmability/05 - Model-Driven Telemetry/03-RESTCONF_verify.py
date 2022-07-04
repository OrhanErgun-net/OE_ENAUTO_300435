import urllib3, requests, json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

Host_IP = "192.168.1.211"
UserName = "OEUser01"
PassWord = "oe123123enauto"
Headers={'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+json'}

URL = f"https://{Host_IP}/restconf/data/Cisco-IOS-XE-mdt-cfg:mdt-config-data"

RES = requests.get(URL,auth = (UserName, PassWord),verify = False, headers = Headers).json()

print (json.dumps(RES, indent=2))
