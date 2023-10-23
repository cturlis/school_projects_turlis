import RPool
import Epool 
import Spool
import CostPool

Round = 1
Elliptical = 2
Square = 3
Quit = 4


def main():
    selection = 0
    while selection != Quit:
        menu()

        selection = int(input("Select pool type "))

        if selection == Round:
            r = int(input("what radius would you like the pool to be in ft? "))
            area = (RPool.RP_area(r))
            per = (RPool.RP_circ(r))
            
        elif selection == Elliptical:
            a = int(input("what length would you like the pool to be in ft? "))
            b = int(input("what width would you like the pool to be in ft? "))
            area =(Epool.EP_area(a,b))
            per =(Epool.EP_circ(a,b))
            
        elif selection == Square:
            s = int(input("what length would you like one side of the pool to be ft? "))
            area =(Spool.SP_area(s))
            per =(Spool.SP_per(s))
            
        elif selection == Quit:
            per = 0
            area = 0
            print("Exiting")
            
        else:
            print("input invalid")
        pcost = (CostPool.Pprice(per))
        acost = (CostPool.Pprice(area))
        both = (acost + pcost) 
        tax = (acost + pcost)*.0635
        total = (both + tax)
        print("your total is",format(total,'.2f'),"$")

        
def menu():
    print("Menu")
    print("1) for round pool")
    print("2) for elliptical pool")
    print("3) for square pool")
    print("4) to quit")
main()

        
