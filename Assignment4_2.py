def AddFactors(no):
    ans=0
    for n in range(1,no):
        if no%n==0:
            ans=ans+n
    return ans

def main():
    print("Enter Number:")
    str=int(input())
    ans=AddFactors(str)
    print("Addition of Factors of {} is {}".format(str,ans))
    

if __name__=="__main__":
    main()
              
        
