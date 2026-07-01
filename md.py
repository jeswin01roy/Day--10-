name ="jeswin"

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
    



