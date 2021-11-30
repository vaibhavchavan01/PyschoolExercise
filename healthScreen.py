#Write a function using 'if/elif/else' conditionals to compute the BMI of a person, 
#and return the risk associated with cardiovascular diseases.
#BMI = weight(kg)/( height(m)*height(m) )
def HealthScreen(weight,height):
    BMI=weight/(height*height)
    print(BMI)
    if(BMI>=27.5):
        print("Your BMI is %d (High Risk)." % BMI)
    elif(BMI>23 and BMI<27.4):
        print("Your BMI is %d (Moderate Risk)." % BMI)
    elif(BMI>18.5 and BMI<22.9):
        print("Your BMI is %d (Low Risk)." % BMI)
    else:
        print("Your BMI is %d (Risk of nutritional deficiency diseases)." % BMI)
a=float(input("enter the weight: "))
b=float(input("enter the height: "))
HealthScreen(a,b)

