

def flip(n):#flip takes the string add the front to the back untill it is fliped completely 
    x = len(n)
    if x == 0:
        return n
    else:
        return flip(n[1:]) + n[0] #add the front to the end of the remaing string 

# the * at the start of the output made this confusing(i was unable to replicate the out put as intended)
def rec_string(n):# rec_string prints the string from the end to the start adding a letter each time 
    x = len(n)
    if x == 0:
        print('x')#prints starting from the end
    else:
        rec_string(n[:x-1])#makes the string get smaller by moving the end position back
        print(n[::-1])#prints starting from the end



def gcd(p,q):#gcd keeps reducing the values(p,q) untill they are the same 
    if q == p:
        return q #if the numbers are the same they can devide eachother
    elif p>q:
        return gcd(p - q, q)# if one side is larger than the other recall and subtract the smaller from the greater
    else:
        return gcd(p,q - p)# same for the other side 
    


def main():
    n = str('abcde')
    p = int(12)
    q = int(8)
    print(flip(n))
    print(' ')
    print(rec_string(flip(n)))#this one i had some trouble with(i used the flip(n)to get the correct output)
    print(' ')
    print(gcd(p,q))
    
    
main()
    
