def NumberOfDigits(no):
    counter=0
    while no!=0:
        no=no//10
        print(no)
        counter=counter+1

    return counter

def main():
    num = int(input("Enter a number: "))
    ans=NumberOfDigits(num)
    print("Number of Digits in {} are {}".format(num,ans))

if __name__=="__main__":
    main()
              
        
