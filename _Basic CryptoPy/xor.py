import base64


text=input("enter text ")
key=input("enter key ")
n=len(text)

cipher=''
for i in range(n):
    t=text[i]
    k=key[i%len(key)]
    x=ord(k)^ord(t)
    cipher+=chr(x)
print(text,key,cipher.encode().hex())

print("hello".encode("utf-8").hex())
print("hello".encode().hex())

print(base64.b64encode(b'nadi'))



