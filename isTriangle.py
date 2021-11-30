#The sum of the lengths of any two sides of a triangle is
#greater than the length of the third side.
def isTriangle(a,b,c):
    if ((a+b)>c) and ((b+c)>a) and ((a+c)>b):
        return True
    else:
        return False
a,b,c=input("Enter the number: ").split()
a=int(a)
b=int(b)
c=int(c)
print(isTriangle(a,b,c))