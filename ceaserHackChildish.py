mess='nadi'
SYMBOLS='abcdefghijklmno'

for key in range(len(SYMBOLS)):
    trans=''

    for s in mess:
        if s in SYMBOLS:
            sindex= SYMBOLS.find(s)
            tindex= sindex-key

            if tindex<0:
                tindex=tindex+len(SYMBOLS)

            trans=trans+SYMBOLS[tindex]
        else:
            trans=trans+s

    print('key #%s: %s' %(key,trans))