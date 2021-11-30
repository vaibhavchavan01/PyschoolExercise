#Write a function isScalene(x, y, z) that accepts the 3 sides of a triangle as inputs. The function should return True if it is a scalene triangle. A scalene triangle has no equal sides.
def isIsosceles(x,y,z):
    if(x==y)or(y==z)or(x==z):
        return False
    else:
        return True
a,b,c=(input("enter the 3 number: ")).split()

print(a,b,c)
print(isIsosceles(a,b,c))
