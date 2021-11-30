#Define a function to determine the standard achieved by a participant taking a physical fitness test.
#The standard is determined based on the individual and total scores for 3 stations.
def Fitness(a,b,c):
    if (a>= 4 and b>= 4 and c>= 4 and a+b+c>=13):
        print("Gold")
    elif(a>=3 and b>=3 and c>=3) and ((a+b+c)>=10):
        print("Silver")
    elif(a>=2 and b>=2 and c>=2) and ((a+b+c)>=7):
        print("Pass")
    else:
        print("Fail")
a= int(input("Enter the 1st station: "))
b= int(input("Enter the 2nd station: "))
c= int(input("Enter the 3rd station: "))
Fitness(a,b,c)