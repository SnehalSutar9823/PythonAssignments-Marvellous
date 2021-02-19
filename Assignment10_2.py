def AdditionOfDigits(no):
    counter=0
    while no!=0:
        ans=no%10
        counter=counter+ans
        no=no//10
        print(no)
        

    return counter

def main():
    num = int(input("Enter a number: "))
    ans=AdditionOfDigits(num)
    print("Addition of Digits in {} are {}".format(num,ans))

if __name__=="__main__":
    main()
              
        
