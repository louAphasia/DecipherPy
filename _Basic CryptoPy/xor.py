import base64


text=input("enter text ")
key=input("enter key ")
n=len(text)

cipher=''
for i in range(n):
    print(i)
    t=text[i]
    print("t=",t)
    k=key[i%len(key)]
    print("k=",k)
    print(ord(k), ord(t))
    x=ord(k)^ord(t)
    print(x)#znak na 10 zapis numer ord()
    cipher+=chr(x) # numer na znak chr()

print(cipher)

print(text,key,cipher.encode().hex())

print("hello".encode("utf-8").hex())
print("hello".encode().hex())

print(base64.b64encode(b'nadi'))



