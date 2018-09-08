import time, os, sys, transCipher, transDecrypt

def main():
    InputFile ='frank.txt'

    OutputFile='franken.txt'

    myKey=10

    myMode='encrypt'


    if not os.path.exists(InputFile):
        print('this file %s not exist. Quitting ...' % (InputFile))
        sys.exit()


    if os.path.exists(OutputFile):
        print('this will be overwrite this file %s (C)ontinue or (Q)uit?' % (OutputFile))

        response = input('>')
        if not response.lower().startswith('c'):
            sys.exit()

    fileObj=open(InputFile, 'r')
    content=fileObj.read()
    fileObj.close()


    print('%sing..' % (myMode.title()))

    startTime=time.time()

    if myMode== 'encrypt' :
        trans= transCipher.encryptMess(myKey, content)
    elif myMode=='decrypt':
        trans=transDecrypt.decrypt(myKey,content)

    totalTime=round(time.time() - startTime,2)

    print('%sion time:%s sec ' % (myMode.title(), totalTime))

    outputFileObj=open(OutputFile, 'w')
    outputFileObj.write(trans)
    outputFileObj.close()

    print('Done  %sing %s (%s characters).' % (myMode, InputFile, len(content)))

    print('%sed file is %s.' % (myMode.title(), OutputFile))

if __name__=='__main__':
    main()