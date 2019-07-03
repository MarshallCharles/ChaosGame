import random as rand
import time

def halfway(a,b):
    return [(a[0]+b[0])/2, (a[1]+b[1])/2]

def random_numbers(options,bounds,iter,cur):
    if iter == 0:
        return cur,iter+1
    elif iter == 1:
        cur = halfway(cur, bounds[rand.choice(options[1:])])
        return cur, iter+1
    else:
        cur = halfway(cur, bounds[rand.choice(options)])
        return cur, iter+1

def main():
    bounds = [(0,0),(1,0),(.5,1)]
    random_numbers(bounds)
if __name__=='__main__':
    main()
