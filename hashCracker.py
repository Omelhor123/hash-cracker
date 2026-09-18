import hashlib
file = 'rockyou.00.txt'
hash = "f806fc5a2a0d5ba2471600758452799c"
#n = hashlib.md5(b"rockyou")
#print(n.hexdigest())
try:
    for word in open(file):
        word = hashlib.md5(word)
        if word.hexdigest() == hash:
            print(word)
except IOError:
    print("{file} not found")

