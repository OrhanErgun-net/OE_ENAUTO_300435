#! /usr/bin/env python
import json
import requests
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

VERIFY_HTTPS = False

if VERIFY_HTTPS is not True:
    disable_warnings(InsecureRequestWarning)

# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


VMANAGE_IP = '10.10.20.90'
USERNAME = 'admin'
PASSWORD = 'C!sco12345'
BASE_URL_STR = 'https://{}:8443/'.format(VMANAGE_IP)

LOGIN_ACTION = 'j_security_check'
LOGIN_DATA = {'j_username' : USERNAME, 'j_password' : PASSWORD}

LOGIN_URL = BASE_URL_STR + LOGIN_ACTION

SESS = requests.session()
LOGIN_RESPONSE = SESS.post(url=LOGIN_URL, data=LOGIN_DATA, verify=False)