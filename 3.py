# 3
# http://www.pythonchallenge.com/pc/def/equality.html
import requests
import re

r = requests.get("http://www.pythonchallenge.com/pc/def/equality.html")
mess = r.text
index = mess.rfind("<!--") + 4


# p = re.compile(ur"[A-Z]{3}[a-z][A-Z]{3}")
m = re.findall("[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]", mess[index:-6])

print(m)

# -->linkedlist
