#Pairwise comparision of DNA sequences is a popular technique used in Bioinformatics. 
# It usually involves some scoring scheme to express the degree of similarity. 
# Write a function that compares two DNA sequences based on the following scoring 
# scheme: +1 for a match, +3 for each consecutive match and -1 for each mismatch.
def pairwiseScore(seqA, seqB):
    count=0
    if(len(seqA)!=len(seqB)):
        print("Not Valid Input")
    else:
        for i in range(0,len(seqA)):
            if(seqA[i]==seqB[i]):
                count+=1
                if(seqA[i-1]==seqB[i-1])and i>=1:
                    count+=2
            else:
                count+=-1
        print(count)
str1=str(input("enter the 1st sequence: "))
str2=str(input("enter the 2nd sequence: "))
pairwiseScore(str1,str2)
