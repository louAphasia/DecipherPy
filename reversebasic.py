


print('foo' in 'f')

print('hello'.find('mnkk'))


print("---------------")

mess = input("wpisz do reverse")
trans = ''

i = len(mess) - 1

while i >= 0:
    trans = trans + mess[i]
    i = i - 1

print(trans)
