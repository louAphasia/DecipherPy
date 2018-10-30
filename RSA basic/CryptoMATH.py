def gcd(a,b):
    while a!=0:
        a,b=b%a,a
    return b


def findModInverse(a,m):
    if gcd(a,m)!=1:
        return None
    u1,u2,u3=1,0,a
    e1,e2,e3=0,1,m

    while e3!=0:
        q=u3//e3
        e1,e2,e3,u1,u2,u3 = (u1-q*e1),(u2-q*e2),(u3-q*e3),e1,e2,e3
    return u1%m
