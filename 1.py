# 1
# http://www.pythonchallenge.com/pc/def/map.html
strL1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc"
strL2 = "dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq"
strL3 = "qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc"
strL4 = "spj."

strOrigin = "abcdefghijklmnopqrstuvwxyz"
strOffset = "cdefghijklmnopqrstuvwxyzab"
strTranst = str.maketrans(strOrigin, strOffset)

print(strL1.translate(strTranst))
print(strL2.translate(strTranst))
print(strL3.translate(strTranst))
print(strL4.translate(strTranst))

strUrl = "http://www.pythonchallenge.com/pc/def/map.html"
print(strUrl.translate(strTranst))
