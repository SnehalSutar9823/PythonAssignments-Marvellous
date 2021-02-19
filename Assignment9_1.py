def PrintFirst10EvenNumber():
    no=2
    counter=0
    while no>=0 and counter <10:
        if no%2==0:
            print(no,end =" ")
            counter=counter+1
            no=no+2


def main():
    print("Below are the first 10 Even numbers on screen")
    
    PrintFirst10EvenNumber()


if __name__=="__main__":
    main()
              
        
