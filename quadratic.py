#For a quadratic equation in the form of ax2 + bx + c, the discriminant, D is b2-4ac.
#Write a function that return the following output depending on the discriminant.
#D > 0: 2 real roots.
#D = 0: 1 real root.
#D < 0: 2 complex roots.
def quadratic(a,b,c):
    d=(b**2)-(4*a*c)
    #print(d)
    if(d>0):
        print("This equation has 2 real roots.")
    elif(d==1):
        print("This equation has 1 real root.")
    else:
        print("This equation has 2 complex roots.")
x=int(input())
y=int(input())
z=int(input())
quadratic(x,y,z)