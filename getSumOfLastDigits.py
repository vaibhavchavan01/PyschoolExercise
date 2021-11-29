#getSumOfLastDigits([2, 3, 4])
 #   9
  #  >>> getSumOfLastDigits([1, 23, 456])
  # 10
def getSumOfLastDigits(numList): 
	a=sum([x%10 for x in numList])
	return a