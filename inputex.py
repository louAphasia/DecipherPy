import sys, time


# input czemu input('>') w transfilecipher wg autora?
print("want you want w or q choice if  q quit?")

response=input('>')

if not response.lower().startswith('w'):
    sys.exit()

print("wwww")

#------------------

print(time.time())
#----------- joiny exercise


list2=['avc','ert','123']

list2='www'.join(list2)

print(list2)


'''mess='ali koty456\
                    pieski'

LETTERS_AND_SPACE='qwertyuiopasdfghjklzxcvbnm'



def removeNonLetters(mess):
    lettersOnly=[]
    for s in mess:
        if s in LETTERS_AND_SPACE:
            lettersOnly.append(s)
    return 'ccc'.join(lettersOnly)

we=removeNonLetters(mess)

print(we)'''