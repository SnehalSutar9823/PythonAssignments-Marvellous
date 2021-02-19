def Divisibleby5(No):
	if No%5==0:
		return True
	else:
		return False

def main():
    number1=int(input("Enter number to check if its divisible by 5 "))
    ans=Divisibleby5(number1)
    if ans==True:
       print("{} is divisible by 5".format(number1))
    else:
       print("{} is not divisible by 5".format(number1))

if __name__=="__main__":
	main()
		
