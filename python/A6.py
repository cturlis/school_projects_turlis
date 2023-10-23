class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def f_enqueue(self, item):
        self.items.insert(0,item)
        
    def dequeue(self):
        return self.items.pop()

    def flip_queue(self):
        return self.items.reverse()
    
    def l_enqueue(self,item):
        self.items.append(item)
    
    def size(self):
        return len(self.items)

    def copy_queue(self):# if the queue was needed after dysplay i would use this
        return self.items.copy()
    
    def print_queue(self):
        for item in self.items:
            print(item, end=" ")
        print()
        
class Employee:

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email=first+'.'+last+'@company.com'
        self.bonus = 0

    def setBonus(self,bonus):
        self.bonus = bonus

    def getBonus(self):
        return self.bonus

    def getPay(self):
        return self.pay

    def setPay(self,pay):
        self.pay = pay
        
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
       

    def __str__(self):
        return 'Employee name: '+self.fullName()+' Employee pay: ' +str(self.pay)+' Employee Bonus: ' +str(self.getBonus())
        
def unload():#unload: takes the files values and puts them into a list then a queue
    pay_list = []
    q = Queue()
    dirany = open("dirany.txt")
    holder = dirany.readlines()#open and take
    p_list = []
    for people in holder:#i used this to get all of the \n(new line spaces) out of the list
        p = people.replace("\n","")#i went through and respaced the list but this could be done for \t also
        p_list.append(p)
    for x in p_list:# after the values are put into a new list they are split
        y = x.split()
        first = y[0]
        last = y[1]#into the parts of everyones data 
        pay = y[2]
        employee = Employee(first,last,pay)#the data is entered into the Employee class
        pay_list.append(pay)
        q.l_enqueue(employee)
    #print(q.print_queue())

    dirany.close()
    #print(pay_list)
    return pay_list,q

def numEmployed(num):
    return 'Number of Employees: '+str(len(num))

def bonusCalc(num):
    per_list = []
    t=0
    bonus_list = []
    for m in range(20,1,-1):#the percent stats at 20 and goes down by 1 
        per = m/100
        per_list.append(per)
    for x in num:
        bonus = float(x)*per_list[t]
        t+=1
        bonus_list.append(int(bonus))
    #print(bonus_list)
    return bonus_list

def bonusTotal(b):
    total=0
    for x in b:
        total+=int(x)
    return total

def bonusSet(q,b):
    nq = Queue()
    b.reverse()
    for x in b:
        employee = q.dequeue()
        employee.setBonus(x)
        nq.f_enqueue(employee)
    #z = nq.dequeue()
    #print(z.getBonus())
    return nq
    
        
def main():
    num,q = unload()
    b = bonusCalc(num)
    bonusTotal(b)
    nq = bonusSet(q,b)# nq = new queue(has bonus)

    #dysplay
    print('---Total data---\n '+str(numEmployed(num))+ ' Total Bonus Paid: '+str(bonusTotal(b)))
    print('')
    nq.flip_queue()
    for x in range(nq.size()):
        people_data = nq.dequeue()
        print(people_data)
    print('--------------------------------------')
    
main()


