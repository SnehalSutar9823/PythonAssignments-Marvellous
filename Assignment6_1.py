def PositiveOrNegative(NO):
    if NO>0:
        return "TRUE"
    elif NO==0:
        return "ZERO"
    else:
        return "FALSE"


def main():
    num=int(input("Enter number"))
    ans=PositiveOrNegative(num)
    if ans=="TRUE":
        print("{} is Positive Number".format(num))
    elif ans=="ZERO":
        print("{} is ZERO".format(num))
    else:
        print("{} is Negative Number".format(num))

if __name__=="__main__":
    main()
              
        
