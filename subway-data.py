import requests
import json
from pprint import pprint

url = 'https://api.odcloud.kr/api/15071311/v1/uddi:b3803d43-ffe3-4d17-9024-fd6cfa37c284'

params = {
    'serviceKey' : 'su2fr9tzcPJq+BgU+cSme24+h06u09KDlAsz6vXctNipdtX6EgkJSo3l1VCZWib8IB8rSlRc+QIeAz0ScidZDg==', 
    'type' : 'json',
    'perPage' : '10', 
    'page' : 1
    }

response = requests.get(url, params=params)

data = json.loads(response.text)

pprint(data)