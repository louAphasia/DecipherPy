import pyperclip

mess='So how to justify obsessive reporting that has no apparent financial rationale, and may even be of little interest to the readers? The answer to this question is central to the idea of a newspaper. If journalism is, in some sense, a public service, then an editor has to understand the ethos of public service – something that is of value to a society without necessarily making a direct financial return. This means thinking of this kind of journalism in the same way you might think of a police, ambulance or fire service. You would, as a citizen, expect such services to be run efficiently, but you would not expect them to have to justify themselves on grounds of profit.'

key=13

mode='encrypt'

SYMBOLS='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890,. !?'

trans=''

for s in mess:
    if s in SYMBOLS:
        sindex=SYMBOLS.find(s)

        if mode=='encrypt':
            transindex=sindex+key
        elif mode=='decrypt':
            transindex=sindex-key

        if transindex>=len(SYMBOLS):
            transindex=transindex-len(SYMBOLS)
        elif transindex<0:
            transindex=transindex+len(SYMBOLS)

        trans=trans+SYMBOLS[transindex]
    else:
        trans=trans+s

print(trans)


