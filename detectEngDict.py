UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower()+'\t\n '

def loadDict():
    dicFile=open('dictionary.txt')

    engwords={}

    for word in dicFile.read().split('\n'):
        engwords[word]=None
    dicFile.close()
    return engwords

ENGLISH_WORDS=loadDict()

def getEngCount(mess):
    mess=mess.upper()
    mess= removeNonLetters(mess)

    possibleWords= mess.split()

    if possibleWords ==[]:
        return 0.0

    matches=0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches +=1
    return float(matches)/len(possibleWords)

def removeNonLetters(mess):
    lettersOnly=[]
    for s in mess:
        if s in LETTERS_AND_SPACE:
            lettersOnly.append(s)
    return ''.join(lettersOnly)

def isEng(mess, wordPercent=20, letterPercent=85):

    wordsMatch = getEngCount(mess)*100>= wordPercent

    numLetters= len(removeNonLetters(mess))

    messLettersPercent = float(numLetters)/ len(mess)*100

    lettersMatch= messLettersPercent>= letterPercent

    return wordsMatch and lettersMatch
