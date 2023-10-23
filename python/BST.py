import random 
import time

class BST():
    def __init__(self,root):
        self.root = root
        self.value = None
        self.left_sub = None
        self.right_sub = None
        

    def insert(self,value):
        if self.root >= value:# if the random makes a duplicate its put on the left side of the tree
            if self.left_sub == None:# if the random makes a duplicate it will make inorder incorrect
                self.left_sub = BST(value)
            else:
                self.left_sub.insert(value)
        else:
            if self.right_sub == None:
                self.right_sub = BST(value)
            else:
                self.right_sub.insert(value)

    def ino(self,ino_list):
        if self.left_sub != None:
            self.left_sub.ino(ino_list)
        ino_list.append(self.root)
        #print(ino_list)
        if self.right_sub != None:
            self.right_sub.ino(ino_list)
    
        
def make_random():
   list_a = [random.randrange(1,1000) for x in range(100000)]
   return list_a
   
            
def main():
    #test_vals = [60,30,35,40,65,55,70]
    #test_tree = BST(50)
    #for nums in test_vals:
        #test_tree.insert(nums)
    #ino_list =[]
    #test_tree.ino(ino_list)
    a_list = make_random()
    tree = BST(random.randrange(1,1000))
    ino_list=[]
    
    start = time.time()
    tree = BST(random.randrange(1,1000))

    for num in a_list:
        tree.insert(num)
    
    tree.ino(ino_list)
    end = time.time()
    print("in-order sort time "+ str(end-start))



    
    print('Done')
    
    

    
main()
            
        
        
            


        
        
