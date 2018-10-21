import pyperclip, detectEngDict,transDecrypt

def main():
    myMess= """ AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e enlh
        na indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no
        euarisfatt e mealefedhsppmgAnlnoe(c -or)alat r lw o eb nglom,Ain
        one dtes ilhetcdba. t tg eturmudg,tfl1e1 v nitiaicynhrCsaemie-sp
        ncgHt nie cetrgmnoa yc r,ieaa toesa- e a0m82e1w shcnth ekh
        gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr
        aBercaeu thllnrshicwsg etriebruaisss d iorr."""

    hackedMess= hackTrans(myMess)

    if hackedMess ==None:
        print('failed')
    else:
        print('Copy hack to clipboard')
        print(hackedMess)
        pyperclip.copy(hackedMess)


def hackTrans(mess):
    print("Hacking...")

    print("Press Ctrl-C or Ctrl-D to quit at any time")

    for key in range(1,len(mess)):
        print('Trying key #%s...' % (key))

        decryptedText= transDecrypt.decrypt(key, mess)

        if detectEngDict.isEng(decryptedText):

            print()
            print("possible encrpyt hack:")
            print('Key %s: %s ' %(key,decryptedText[:100]))
            print()
            print('Enter D for done or just press Enter to cont hacking')

            response=input('>')

            if response.strip().upper().startswith('D'):
                return decryptedText

    return None

if __name__== '__main__':
    main()
