import requests

TOKEN = '***'   #ТОКЕН!!!
PREPAREUPLOADURL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
params = {'path': '/1.txt', 'overwrite': 'true'}
headers = {'Accept': 'application/json', 'Authorization': TOKEN}

file_path = '1.txt'

response = requests.get(PREPAREUPLOADURL, params=params, headers=headers)
print(response.text)

puturl = response.json().get('href')
print(puturl)

files = {'file': open(file_path, 'rb')}
response = requests.put(puturl, files=files, headers=headers)
print(response)
