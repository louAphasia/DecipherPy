import random,sys, transCipher, transDecrypt

def main():

    random.seed(12)
    for i in range(20): #testy

        mess='qwertyuiopasdfghjklzxcvbnm'* random.randint(2,10)

        mess=list(mess)
        random.shuffle(mess)

        mess=''.join(mess)

        print('test #%s: "%s"'% (i+1, mess[:10]))

        for key in range(1,int(len(mess)/2)):
                encrypted=transCipher.encryptMess(key,mess)
                decrypted=transDecrypt.decrypt(key,encrypted)


                if mess!=decrypted:
                    print('misamtach key%s and mess %s' % (key,mess))

                    print('decrypted as '+ decrypted)

                    sys.exit()

    print('test passed')

if __name__== '__main__' :
    main()


