def sequential_search(a_list, item):
  pos = 0
  count = 0
  found = False
  while pos < len(a_list) and not found:
    if a_list[pos] == item:
      found = True
      count = pos+1 #index starts from 0 so +1 is the count of times its checked a position
    else:
        count= (len(a_list)) #if not found it will check the whole list
        pos = pos+1 #uses positions ideration to get count
  return found, count


test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequential_search(test_list, 3))
print(sequential_search(test_list, 13))
