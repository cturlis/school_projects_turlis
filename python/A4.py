
import time
A = list(input("input of list A:"))

##----test----## ## I used this to see how the two algos fare with list of very large sizes
#A=[] 
#m = int(input("list size:"))
#for z in range(m):
   # A.append(z)
##----test-----##   
B = {}
All = {'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1, '1':1,'2':1,'3':1,'4':1,'5':1,'6':1,'7':1,'8':1,'9':1}


##----1----##  "Big-O(N)"== (log(N))


start_time1 = time.time()
for x in A:
    multi = A.count(x)
    if multi > 1:
        y = 1
    else:
        y = 2
        break
if y == 1:
    print("false")
else:
    print("true")
end_time1 =time.time()
ex1_time = end_time1 - start_time1


##----2----##  "Big-O(N)"== (N)


start_time2 = time.time()
for x in A:
    if x in B:
        B[x] += 1
    else:
        B[x] = 1

check = (set(B.values()) <= set(All.values()))
if check == True:
    print("true")
else:
    print("false")
end_time2 =time.time()
ex2_time = end_time2 - start_time2

## one is much faster then two ##
print("1st")
print(ex1_time)
print("2nd")
print(ex2_time)


