def ordered_sequential_search(a_list, item):
  pos = 0
  count = 0
  found = False
  stop = False
  while pos < len(a_list) and not found and not stop:
    if a_list[pos] == item:
       found = True
       count = pos+1 #if found count is the position +1 since indexes start at 0
    else:
       if a_list[pos] > item:
        stop = True
        count = pos+1 #has to check one after where the number should be so is pos +1 
       else:
        pos = pos+1 #uses position as iderater
  return found, count
   
test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(ordered_sequential_search(test_list, 3))
print(ordered_sequential_search(test_list, 13))
