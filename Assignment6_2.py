def DisplayPattern(no):
    for n in range(no):
        for n1 in range(no,n,-1):
            #print("n1",n1)
            #print("no",no)
            print("*",end=" ")
        print("")

def main():
    num = int(input("Enter a number: "))
    ans=DisplayPattern(num)
    

if __name__=="__main__":
    main()
              
        
