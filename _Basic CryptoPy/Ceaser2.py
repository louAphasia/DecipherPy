# need 2 helper mappings, from letters to ints and the inverse
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))
I2L = dict(zip(range(26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

key = 'pies'
plaintext = "DEFEND THE EAST WALL OF THE CASTLE"

message = "ljust a simple test!"
key = 3
coded_message = ""
for ch in message:
    code_val = ord(ch) + key
    if ch.isalpha():
        if code_val > ord('z'):
            code_val -= ord('z') - ord('a')
        coded_message = coded_message + chr(code_val)
    else:
        coded_message = coded_message + ch
print(message)
print(coded_message)


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
