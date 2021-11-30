#Write a function that determines if a given year is a leap year.
#A leap year is divisible by 4, but not by 100, unless it is also divisible by 400.
def leapyear(year):
    if(year%4==0 and year%100!=0)or (year%400==0):
        print("True")
    else:
        print("False")
a=int(input("enter the year: "))
leapyear(a)