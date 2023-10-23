import random,itertools
from random import randrange

t=1
i=2
n=3
H=4

def main():
    c = [''.join(x) for x in itertools.permutations('1234', 4)]
    for w in range(25):
        print(c)
    
main()
    
