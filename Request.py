import requests
from requests import HTTPError
response = requests.get('https://www.engineerspock.com/')
print(response) 

for url in ['https://www.engineerspock.com/', 'https://www.engineerspock.com/djhasjkfaw']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'Error: {http_err}')
    except Exception as err:
        print(f'Unknown error:{err}')
    else:
        print('Connected Successfully')

response = requests.get('https://www.engineerspock.com/')
print(response.content)
response = requests.get('https://api.github.com/')
data = response.json()
print(data)

print(response.headers, end='\n')

from getpass import getpass
uth_response = requests.get('https://api.github.com/user', auth=('mrSnail04', getpass()))

#для отработки таймаутов
from requests.exceptions import Timeout
try:
    response = requests.get('https://api.github.com/', timeout = 1)
except Timeout:
    print('The request timed out')

#адаптеры
from getpass import getpass
from requests.adapters import HTTPAdapter
adapter = HTTPAdapter(max_retries=3)
with requests.Session() as session:
    session.mount('https://api.github.com/', adapter)
    session.auth = ('mrSnail04', getpass())
    try:
        session.get('https://api.github.com/user')
    except ConnectionError as err:
        print(f'Failed to connect: {err}')
    else:
        print('ok')