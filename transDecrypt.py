import math

def main():
    mess='niosa vdle'
    key=3

    plaintext=decrypt(key,mess)
    print(plaintext+ '|')

def decrypt(key,mess):
    nrCo=int(math.ceil(len(mess)/float(key)))
    nroR=key
    nroSha=(nrCo*nroR)-len(mess)

    plaintext=['']*nrCo

    co=0
    ro=0

    for s in mess:
        plaintext[co]+=s
        co+=1

        if (co == nrCo) or (co == nrCo - 1 and ro >= nroR - nroSha):
            co = 0
            ro += 1

    return ''.join(plaintext)

if __name__=='__main__':
    main()
