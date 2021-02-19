def CheckPrime(no):
    counter=0
    print(counter)
    if no > 1:
        for i in range(2,no):
            print("i {}",format(i))
            if (no % i) == 0:
                counter=counter+i
                print("Counter {}",format(counter))
                
    if counter==0:
            return True     


def main():
    num = int(input("Enter a number: "))
    ans=CheckPrime(num)
    if ans==True:
        print("{} is Prime Number".format(num))
    else:
        print("{} is Not Prime Number".format(num))

if __name__=="__main__":
    main()
              
        
