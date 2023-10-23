import time 

def factorail(n):
    
    if n == 0:#base
        return 1
    product = n* factorail(n-1)#f call its self 
    return product

def main():
    print(factorail(10))
main()
