# need 2 helper mappings, from letters to ints and the inverse
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

key ='pies'
plaintext = "DEFEND THE EAST WALL OF THE CASTLE"

def shift(key):
    klist=[]
    for x in range(len(key)):
        klist.append(ord(key[x]))

    print(klist)

shift(key)
'''
# encipher
ciphertext = ""
for c in plaintext.upper():
    if c.isalpha(): ciphertext += I2L[ (L2I[c] + p)%26 ]
    else: ciphertext += c

# decipher
plaintext2 = ""
for c in ciphertext.upper():
    if c.isalpha(): plaintext2 += I2L[ (L2I[c] - key)%26 ]
    else: plaintext2 += c

print(plaintext)
print(ciphertext)
print(plaintext2)
'''