import json
import os
import urllib.request
from urllib.request import Request, urlopen

url =" https://cynbus.com/api/v1/home/dbake/"
req = Request(
    url=url, 
    headers={'User-Agent': 'Mozilla/5.0'}
)
webpage = urlopen(req).read()
response = urllib.request.urlopen(url)
data = response.read()
dict = json.loads(data)
print(dict)