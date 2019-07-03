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
def numbers_to_file(options,bounds,amt,cur):
    file = open('fractaldata.csv', 'a')
    file.write('x,y')
    file.write('\n')
    iter = 0

    try:
        while iter < int(amt):
            cur,iter = random_numbers(options,bounds,iter,cur)
            file.write(str(cur[0])+','+str(cur[1]))
            file.write('\n')
        file.close()
        print("Done")
        return
    except KeyboardInterrupt:
        print("ITER IS",iter)

def main():
    '''#TRIANGLE'''
    # cur = [0,0]
    # bounds = [(0,0),(1,0),(.5,1)]

    '''#PENTAGON'''
    bounds = [(.2,0),(.8,0),(.5,1),(0,.6),(1,.6)]
    cur = [.2,0]
    
    options = []
    for i in range(len(bounds)):
        options.append(i)
    file = open('fractaldata.csv', 'w').close()
    amt = input("How many datapoints: ")
    numbers_to_file(options,bounds,amt,cur)
if __name__=='__main__':
    main()
