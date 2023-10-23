import math
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def main():
   n = input("input word to be checked: ")
   print(check_palin(n))
   num = input("enter numbers: ")
   print(getStat(num))
    
def check_palin(n):
    is_true = 0
    nope = False
    s = Stack()#used to flip with a loop into stack s2
    s1 = Stack()#original stack order
    s2 = Stack()#fliped stack order
    #n = input("input word to be checked: ")
    for i in n:#make stack s1 and s
        s.push(i)
        s1.push(i)
    for z in n:#destroy stack s to make s2(fliped)
        r=Stack.pop(s)
        s2.push(r)
    for x in range(len(n)):#compare all items in stack s1 and s2
        check1 = s1.pop()
        check2 = s2.pop()
        if check1 == check2:
            is_true = 1
        else:
            nope = True
    if nope == False and is_true == 1:#out put if stack is palindrome and not empty
        return 'True'
    else:
        return 'false'


def getStat(num):
    num_stack = Stack()
    num_list=[]
    for numbers in num:# make stack
        num_stack.push(numbers)
        p = int(num_stack.pop())# undo stack into list to use min,max,sum
        num_list.append(p)
    return("max:",str(max(num_list)),"min:",str(min(num_list)),"sum:",(sum(num_list)))
    for fix in num:# rebuild stack 
        num_stack.push(fix)
    
main()    





















    
