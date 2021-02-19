from ModuleArithematic import *


def main():
    print("Enter 2 numbers for Arithematic Operations")
    no1=int(input())
    no2=int(input())

    ans1=Add(no1,no2)
    ans2=Sub(no1,no2)
    ans3=Mul(no1,no2)
    ans4=Div(no1,no2)

    print("Addition of {} and {} is {}".format(no1,no2,ans1))
    print("Substraction of {} and {} is {}".format(no1,no2,ans2))
    print("Multiplication of {} and {} is {}".format(no1,no2,ans3))   
    print("Division of {} and {} is {}".format(no1,no2,ans4))
    
if __name__=="__main__":
    main()
