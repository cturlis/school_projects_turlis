class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0,item)
        
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def print_queue(self):
        for item in self.items:
            print(item, end=" ")
        print()
        
    def del_3(self):
        y = self.size()
        hold = []
        for x in range(y):
            z = self.dequeue()
            hold.append(z)
        hold.reverse()
        hold.pop(2)
        hold.reverse()
        for m in hold:
            self.enqueue(m)
        return self.items
            
        
       
 
def main():
    q = Queue()
    q.enqueue(5)
    q.enqueue(4)
    q.enqueue(3)
    q.enqueue(2)
    q.enqueue(1)
    print(q.print_queue())
    q.del_3()
    print(q.print_queue())
main()
