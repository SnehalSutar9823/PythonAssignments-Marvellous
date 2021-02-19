def Factorial(no):
    ans=1
    for n in range(no):
        ans=(ans)+(ans*n)
    return ans

def main():
    print("Enter Number:")
    str=int(input())
    ans=Factorial(str)
    print("Factorial of {} is {}".format(str,ans))
    

if __name__=="__main__":
    main()
              
        
