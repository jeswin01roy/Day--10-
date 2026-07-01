# reccursive function for factorial
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
    

#sum of n numbers
def sum(n):
    if(n==0):
        return 0
    else:
        return n+sum(n-1)

#main function
def main():
    while(True):
        print("\t\t factorial or sum usingrecursive")
        num= int(input("enter the range:"))
        choice= int(input("select the choice \n1.factorial\n2.sum of range\n3.stop\n choice: "))
        if(choice==1): 
            print(f"\nthe factorial of {num} is:",fact(num))
        elif(choice==2):   
            print(f"\nthe sum of  zero to {num} is:",sum(num))
        elif(choice==3):
            break
        else:
            print("invalid entry")
main()