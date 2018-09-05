import pyperclip


def main():
    mess = 'nadi'
    key = 3

    citext= encryptMess(key, mess)

    print(citext +'|')

    pyperclip.copy(citext)



def encryptMess(key,mess):
    citext= [''] * key

    for column in range(key):
        currenti = column

        while currenti < len(mess):
            citext[column] += mess[currenti]
            currenti += key


    return ''.join(citext)

if __name__== '__main__':
    main()