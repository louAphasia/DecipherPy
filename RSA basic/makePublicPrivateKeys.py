import random,sys,os, PRIMESNum, CryptoMATH

def main():

    print('Make files')
    makeKeyFiles('nadisnowdi',1024)
    print("Key files made.")

def generatorKey(keySize):
    p=0
    q=0
    #Step 1 PRIMES p i q
    while p==q:
        p=PRIMESNum.generateLargePrime(keySize)
        q=PRIMESNum.generateLargePrime(keySize)

    n=p*q

    #step 2 create e

    print("generating e prime relative to p-1(q-1)")
    while True:
        e=random.randrange(2**(keySize-1),2**(keySize))
        if CryptoMATH.gcd(e,(p-1)*(q-1))==1:
            break

    # step 3 the mod inverse of e
    print ("Generating d mod inverse of e" )
    d=CryptoMATH.findModInverse(e,(p-1)*(q-1))

    publicKey=(n,e)
    privateKey=(n,d)
    print(publicKey + "ccc"+ privateKey)

    return (publicKey,privateKey)

def makeKeyFiles(name,keySize):




