from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)


cipher=AES.new(key,AES.MODE_ECB)

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data=b'1234567890' #musi byc bytowe
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC)
ciphertext, tag = cipher.encrypt_and_digest(data)

file_out = open("encrypted.bin", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]



#ciphertext, tag = cipher.encrypt_and_digest(data)
#data = cipher.decrypt_and_verify(ciphertext, tag)
#file_out = open("encrypted.bin", "wb")
#[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]



#file_in = open("encrypted.bin", "rb")
#nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

# let's assume that the key is somehow available again


