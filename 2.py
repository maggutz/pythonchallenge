# 2
# http://www.pythonchallenge.com/pc/def/ocr.html
import requests
from collections import Counter

r = requests.get("http://www.pythonchallenge.com/pc/def/ocr.html")

mess = r.text
index = mess.rfind("<!--") + 4

# print(mess[index:-6])
print(Counter(mess[index:-6]).most_common())
# elatuqyi

print(mess.rfind("e"))
print(mess.rfind("q"))
print(mess.rfind("u"))
print(mess.rfind("a"))
print(mess.rfind("l"))
print(mess.rfind("i"))
print(mess.rfind("t"))
print(mess.rfind("y"))


# --> equality
# --> http://www.pythonchallenge.com/pc/def/equality.html
