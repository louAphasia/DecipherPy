import hashlib

x=hashlib.new("sha1","HELLO".encode("utf-16le")).hexdigest()  # moze byc utf-8 zamiast utf-16le

print(x)