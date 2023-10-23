import random
# Implementation of an Unordered List ADT as a linked list.  The list
# is accessed through a reference to the first element, head.  
# Adopted from the textbook.

class Node:
    '''
    Create a Node object and initialize its data.  
    '''
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        
    '''
    Accessor for node data
    '''
    def get_data(self):
        return self.data
    
    '''
    Accessor for next reference
    '''
    def get_next(self):
        return self.next
    
    '''
    Mutator for node data
    '''
    def set_data(self, new_data):
            self.data = new_data
            
    '''
    Mutator for next reference
    '''
    def set_next(self, new_next):
            self.next = new_next

    def del_node(self):
        self.data = None 

class UnorderedList:
    '''
    List is empty upon creation and the head reference is None
    '''
    def __init__(self):
        self.head = None    
        
    '''
    Returns True if list is empty, False otherwise
    '''
    def is_empty(self):
        return self.head == None

    def print_list(self):
        val_list = []
        current = self.head
        while current != None:
            vals = current.get_data()
            val_list.append(vals)
            current = current.get_next()
        return val_list
            
    def replace_element(self,i,new_val):
        current = self.head
        for place in range(i):
            current = current.get_next()
        return current.set_data(new_val)

    #index(item) returns the position of item in the list. It needs the item and 
    #returns the index. Assume the item is in the list.
    #Assumes item is on list, if not will fail 
        
    def index(self,item):#item is to be checked for multiplicity
        found = False    #has a small chance to fail if 5 is not picked in random numbers(see main())
        index = 0
        current = self.head
        if current.get_data() == item:
            return 'index: '+ str(index) 
        while current != None or not found:
            current = current.get_next()
            index += 1
            if current.get_data() == item:
                found = True
                return 'item '+str(item)+' index: ' + str(index)#returns index
            else:
                found = False
                
    #pop() removes and returns the last item in the list. It needs nothing and 
    #returns an item. Assume the list has at least one item.

    def pop(self):
        current = self.head
        previous = None
        found = False
        while not found:
            previous = current
            current = current.get_next()
            if current == None and not previous == None :
                data = previous.get_data()
                previous.del_node()
                self.remove(None)
                return 'last item removed:'+str(data)#removes last item and returns it 
            
    #pop_pos(pos) removes and returns the item at position pos. It needs the
    #position and returns the item. Assume the item is in the list.
    

    def pop_pos(self,pos):#pos is position to be removed
        current = self.head
        for place in range(pos):
            current = current.get_next()
        data = current.get_data()
        current.del_node()
        self.remove(None)
        return 'Item removed from position '+str(pos)+': '+str(data)#returns removed item

    #a function that counts the number of times an item occurs in the linked list


    def count(self,item):# item is checked for multiplicity
        counter = 0
        current = self.head
        previous = None
        found = False
        if current.get_data() == item:
            counter = 1
        while not found:
            previous = current
            current = current.get_next()
            if current == None and not previous == None:
                return 'number of '+str(item)+'s in list: ' +str(counter)#returns times a number repeats
            if current.get_data() == item:
                counter += 1

    #a function that would delete the replicate items in the linked list
                
    def del_rep(self):
        sort = []#flips list to ascending order
        t_list = self.print_list()
        v_list = list(set(t_list))
        t_list = UnorderedList()
        for data in v_list:
            sort.append(data)
        sort.reverse()
        for val in sort:
            t_list.addItem(val)
        return t_list #returns list with no repetitions (see main())


        


    
    '''
    Add an element to head of the list
    '''
    def addItem(self, item):
        # Create a node using item as its data
        temp = Node(item)
        # make the next reference of the new node refer to the head 
        # of the list
        temp.set_next(self.head)
        # modify the list head so that it references the new node
        self.head = temp
        
    '''
    Returns the size of the list
    '''
    def size(self):
        # start at the head of the list
        current = self.head
        count = 0
        # Traverse the list one element at a time.  We know
        # we reached the end when the next reference is None
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    '''
    Search for an item in the list.  Returns True if found, False otherise.  
    '''
    def search(self,item):
        current = self.head
        found = False
        # As long as the element is not found and we haven't 
        # reached the end of the list
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                # go to the next element
                current = current.get_next()
        return found
    
    '''
    Remove the first occurrence of item from the list.  
    '''
    def remove(self, item):
        # keep track of current and previous elements
        current = self.head
        previous = None
        found = False
        # traverse the list 
        while current != None and not found:
            # if we have a match, stop
            if current.get_data() == item:
                found = True
            # otherwise advance current and next references
            else:
                previous = current
                current = current.get_next()
           
        # the element to be deleted is the head of the list     
        if found:
            if previous == None:
                self.head = current.get_next()
                # the element to be deleted is not the head
            else:
                previous.set_next(current.get_next())
          
          
def main():
    h_list = UnorderedList()
    sorter = []#sorts list into ascending order
    for x in range(0,15):
        data = random.randint(1,5)
        sorter.append(data)
    sorter.sort()
    sorter.reverse()
    for vals in sorter:
        h_list.addItem(vals)
    print(h_list.print_list())
    print(h_list.index(5))#will fail if not in list(see Linked lists assignment PDF)
    print(h_list.pop())
    print(h_list.pop_pos(2))
    print(h_list.print_list())
    print(h_list.count(1))
    print(h_list.count(2))
    print(h_list.count(3))
    print(h_list.count(4))
    print(h_list.count(5))
    h_list = h_list.del_rep() #make sure to use the same varaible name as the original list for convenience
    print(h_list.print_list())
    

    print('end')
    
main()
