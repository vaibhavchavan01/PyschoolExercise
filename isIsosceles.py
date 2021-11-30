def isIsosceles(x,y,z):
    if(x==y)or(y==z)or(x==z):
        return True
    else:
        return False
a,b,c=int(input("enter the 3 number: ")).split()
print(isIsosceles(a,b,c))
#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 -personal access token