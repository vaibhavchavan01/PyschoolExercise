import math
def isPrime(num):
    a=(num/2)
    flag=0
    for i in range(2,int(a)):
        if num%i==0:
            flag=1
            break
    if(flag==1):
        print("False") 
    else:
        print("True")
n=int(input("enter the no.: "))
if(n<=1):
    print("False")
else:
    isPrime(n)