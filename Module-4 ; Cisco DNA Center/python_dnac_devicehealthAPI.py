import requests
import json

url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/site-health"

payload={}
headers = {
  'x-auth-token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MjQxOTIzZTU3MjU5NTA2YTU2YjRhYTEiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjYyM2YwMjlhNTcyNTk1MDZhNTZhZDljNCJdLCJ0ZW5hbnRJZCI6IjYyM2YwMjk4NTcyNTk1MDZhNTZhZDliZCIsImV4cCI6MTY1Njc2NjQ5NywiaWF0IjoxNjU2NzYyODk3LCJqdGkiOiJiYzVjMmI2NS0yMjBlLTQ0ZDUtOGM4OS1hYzljYjk5YTc0MWYiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.vSSB0ftoInYzErG8Uh9Vzl4_Fs_tS6UGJjJbNMzSWkEp6XDp4N4p158rj1eH3cQE6c3n-rwD1Dr9_pt61buXtuE7xAePhhpmw4fNDlf_EfdOqdgo9aymBLfWa10_4ymQ2gkcqWEjs9sAwzYBHpDOcW0zRiYLUGXwOdoMN_c4femZdCLYx9K2fjTU_OjPZV14Oi3j2MAqKjThHBkupzedyY13fxK_-q6lEk5rE3K2cxlG1XNPQG2ajQiqVldj8rQpmmDbSj772neAHG9lIkF8Ozl_08YHRZo5pJKWIWVNfbNWW-loKvflQyctDjBRnWiDT1jBJtqsl-zK20ZSz1jLRw',
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)