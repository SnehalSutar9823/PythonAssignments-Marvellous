def DisplayPattern(no):
    for n in range(no+1):
        for n1 in range(n):
            #print("n1",n1)
            #print("no",no)
            print(n1+1,end=" ")
        print("")

def main():
    num = int(input("Enter a number: "))
    ans=DisplayPattern(num)
    

if __name__=="__main__":
    main()
              
        
