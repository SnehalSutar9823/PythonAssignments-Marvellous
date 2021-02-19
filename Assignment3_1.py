def Add(no1,no2):
	return no1+no2
	
def main():
	number1=int(input("Enter First Number"))
	number2=int(input("Enter First Number"))
	
	ans=Add(number1,number2)
	print("Addition of {} and {} is {}".format(number1,number2,ans))

if __name__=="__main__":
	main()
