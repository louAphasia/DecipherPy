

def pow(a,k,n):
    b=bin(k)[2:]
    m=len(b)
    r=1
    x=a%n

    for i in range(m-1,-1,-1):
        if b[i]=='1':
            r=r*x%n
        x**=2
        x%=n
    return r

print(pow(2,126,75))