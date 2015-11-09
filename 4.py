# 4
# http://www.pythonchallenge.com/pc/def/linkedlist.php
import urllib.request
import string

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
url_value = "12345"

for i in range(1,550):
    full_url = url + url_value
    data = urllib.request.urlopen(full_url)
    url_value = data.read()
    nothing_value = str(url_value)
    nothing_index = nothing_value.rfind(" ")
    url_value = nothing_value[nothing_index+1:-1]
    if url_value == "going.":
        url_value = str(16044/2)
    print(str(i) + ": " + nothing_value)

# Ver 0.1
# 85: b'and the next nothing is 16044'
# 86: b'Yes. Divide by two and keep going.'
# 277: b'peak.html'
# 399: b'and the next nothing is 18330'

# Ver 0.2
#    if url_value == "going.":
#        url_value = str(16044/2)
# 85: b'and the next nothing is 16044'
# 86: b'Yes. Divide by two and keep going.'
# 87: b'and the next nothing is 25357'
# 140: b'and the next nothing is 82682'
# 141: b'There maybe misleading numbers in the \ntext. One example is 82683. Look only for the next nothing and the next nothing is 63579'
# 250: b'and the next nothing is 66831'
# 251: b'peak.html'
# 399: b'and the next nothing is 21816'
# 442: b'peak.html'
# 441: b'and the next nothing is 66831'

# --> peak.html
# --> http://www.pythonchallenge.com/pc/def/peak.html
