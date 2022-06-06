#!/usr/bin/env python3
#!/usr/bin/env python3
import libnum
#生成随机素数
def rsa_def(e,m):
    p=libnum.generate_prime(1024)
    q=libnum.generate_prime(1024)
    n=p*q
    c=pow(m,e,n)
    n_lt.append(n)
    c_lt.append(c)

n_lt=[]
c_lt=[]
e=13
m= 45
for i in range(13):
    rsa_def(e,m)
print("e=",e)
print("n=",n_lt)
print("c=",c_lt)
