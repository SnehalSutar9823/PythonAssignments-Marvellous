def DisplayPattern(no):
    for n in range(no):
        for x in range(no):
            print("*",end=" ")
        print("")

def main():
    print("Enter Number:")
    str=int(input())
    ans=DisplayPattern(str)
    

if __name__=="__main__":
    main()
              
        
