
def binary_search(a_list, item, count):
    if len(a_list) == 0:
       return False, count
    else:
       midpoint = len(a_list) // 2
       count+=1
       if a_list[midpoint] == item:
         return True, count
       else:
         if item < a_list[midpoint]:
            return binary_search(a_list[:midpoint], item, count)
         else:
            return binary_search(a_list[midpoint + 1:], item,count)

        
