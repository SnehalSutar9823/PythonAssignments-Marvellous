def ChkNum(No):
	if No%2==0:
		return True
	else:
		return False


if __name__=="__main__":
	number1=int(input("Enter number to check if its even or odd"))
	
	ans=ChkNum(number1)
	if ans==True:
	   print("{} is Even".format(number1))
	else:
	   print("{} is Odd".format(number1))
		
