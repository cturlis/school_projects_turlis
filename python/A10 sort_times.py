
import random 
import time
import math 

def bubble_sort(a_list):
   start = time.time()
   for pass_num in range(len(a_list) - 1, 0, -1):
      for i in range(pass_num):
         if a_list[i] > a_list[i + 1]:
            temp = a_list[i]
            a_list[i] = a_list[i + 1]
            a_list[i + 1] = temp
   end = time.time()
   return 'bubble sort time: '+ str(end - start)#, a_list


def selection_sort(a_list):
   start = time.time()
   for fill_slot in range(len(a_list) - 1, 0, -1):
      pos_of_max = 0
      for location in range(1, fill_slot + 1):
         if a_list[location] > a_list[pos_of_max]:
            pos_of_max = location
      temp = a_list[fill_slot]
      a_list[fill_slot] = a_list[pos_of_max]
      a_list[pos_of_max] = temp
   end = time.time()
   return 'selection sort time: '+ str(end - start)



def merge_sort(a_list):
    #print("Splitting ", a_list)
    start = time.time()
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i=0 
        j=0 
        k=0
        while i < len(left_half) and j < len(right_half): 
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i=i+1
            else:
                a_list[k] = right_half[j] 
                j=j+1
            k=k+1
        while i < len(left_half): 
            a_list[k] = left_half[i] 
            i=i+1
            k=k+1
        while j < len(right_half): 
            a_list[k] = right_half[j] 
            j=j+1
            k=k+1
    end = time.time()
    #return("Merging ", a_list)
    return 'merge sort time: '+ str(end - start)#,a_list
            
def make_list():
   list_a = [random.randrange(1,100) for x in range(50000)]
   return list_a




def main():
   a_list = make_list()
   #b_list = make_list()
   #c_list = make_list()
   print(selection_sort(a_list))
   print(bubble_sort(a_list))
   print(merge_sort(a_list))
   

main()


