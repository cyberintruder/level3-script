#!/usr/bin/env python
 
from bs4 import BeautifulSoup
import urllib2 
import re 
import base64
import hmac 
import hashlib
import datetime
 
#considered key is = '2018-05-13'
for k in range(2018, 2030):
    for j in range(5, 13):
        found = False
        for i in range(1, 32):
            if((j==2) & (k%4==0) & (i>=30)):
                continue
            elif((j==2) & (k%4!=0) & (i>=29)):
                continue
            elif(((j==4) | (j==6) | (j==8) | (j==9) | (j==11)) & (i>=31)):
                continue
            else:
                year = k
                month = j
                date = i
                key1 = datetime.date(year, month, date).strftime('%Y-%m-%d')
                print key1
                value = 'e7i8fndc-kyx0-zxqzyoso-g687oog7zlms769s'
                html_request  = urllib2.Request("http://" +"ec2-34-207-132-244.compute-1.amazonaws.com/levels/6")
                html_request.add_header('Host', 'ec2-34-207-132-244.compute-1.amazonaws.com')
                html_request.add_header('Cookie', '_sncpractical_session=MGxGSHpWSUNmZk44S3UyeEdQczhaVnhtRDl3NkpMZWNhaGVZNnVjRFFvSWhtYkVxV1FQTW9IcDFQUHJDSkpPM0J6OTE0S3Z4aTlYVFZVaXY0eGJVeWdPQml6VUlxa2hGSjRQeEh3cTJFdjFMV0FJd0V0SExOeUt5TkF3anVQaXZ3Vm13YTJrUkJKVEtSTXRpNUtEdVBXSGZxZ1RqeHp3cXlQQzI2MUg0SFo4eDNzbkVYMnorcXZpL1Y4ejZ2RzRiRmFoT0tiUUdxaUx4ZTFJOE15a2RBZzB2N2V1SG00a0RCeTJ0WWFaK2JFST0tLXk0aGh4cVhwU1JJTEk0ZVlRcnFBWFE9PQ%3D%3D--4a4a1df90d48a4d89796293ccfabd8790f8d10f9')
                html_request.add_header('Connection', 'close')
                html_request.add_header('Upgrade-Insecure-Requests', '1')
                html_request.add_header('X-Authorization-Date', key1)
                html_request.add_header('X-Session-Id', value)
                data = value
                hmac1 = hmac.new(key1, data.encode('UTF-8'), hashlib.sha1)
                signature = hmac1.digest().encode('hex')
                html_request.add_header('X-Signature-AllComp', signature)  
                html = urllib2.urlopen(html_request).read()
                print html
                soup = BeautifulSoup(html, "lxml")
 
                if "The Password for this level is:" in html:
                    search_string = 'The Password for this level is:'
                    start_pos = html.find(search_string)
                    print html[start_pos: start_pos+50]
                    found = True
                    break
                else:
                 print" Password not Found"
        if(found):
            break
    if(found):
        break


