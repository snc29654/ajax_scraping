import cgi
import cgitb
import json
import sys
import io
import requests
from bs4 import BeautifulSoup
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


cgitb.enable()
form=cgi.FieldStorage()
data=form.getvalue("sent")
receive=data


site = requests.get(data)
data = BeautifulSoup(site.text, 'html.parser')
find_data=data.find_all("a")




print("Content-type: text/html\n")
print(find_data)
