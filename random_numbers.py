import random as rand
import time
import argparse

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
def no_prev_vertex(amt,options,bounds,iter,cur):
    file = open('fractaldata.csv', 'a')
    file.write('x,y')
    file.write('\n')
    try:
        while iter < int(amt):
            if iter == 0:
                file.write(str(cur[0])+','+str(cur[1]))
                file.write('\n')
                iter += 1
            elif iter == 1:
                num = rand.choice(options[1:])
                vertex = bounds[rand.choice(options[1:])]
                cur = halfway(cur,vertex )
                file.write(str(cur[0])+','+str(cur[1]))
                file.write('\n')
                iter += 1
                prev = cur
            else:
                num1 = num
                options.remove(num)
                num = rand.choice(options)
                options.append(num1)
                vertex = bounds[num]
                cur = halfway(cur, vertex)
                file.write(str(cur[0])+','+str(cur[1]))
                file.write('\n')
                iter += 1
                prev = cur
        file.close()
        print("Done")
        return
    except KeyboardInterrupt:
        print("ITER IS",iter)
        return

def numbers_to_file(options,bounds,amt,cur,flag):
    iter = 0
    print(flag)
    if flag == 1:

        no_prev_vertex(amt,options,bounds,iter,cur)
    else:
        file = open('fractaldata.csv', 'a')
        file.write('x,y')
        file.write('\n')
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
    return

def main():
    flag = 0
    parser = argparse.ArgumentParser("Description = Chaos Game Fractals!")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-n', '--npv', action = 'store_true', help = 'Next vertex cannot be the previous vertex')
    args = parser.parse_args()
    if args.npv == True: flag = 1
    
    '''TRIANGLE'''
    # cur = [0,0]
    # bounds = [(0,0),(1,0),(.5,1)]

    '''PENTAGON'''
    bounds = [(.2,0),(.8,0),(.5,1),(0,.6),(1,.6)]
    cur = [.2,0]
    '''Square '''
    # bounds = [(0,0),(0,1),(1,0),(1,1)]
    # cur = [0,0]

    options = []
    for i in range(len(bounds)):
        options.append(i)
    file = open('fractaldata.csv', 'w').close()
    amt = input("How many datapoints: ")
    numbers_to_file(options,bounds,amt,cur,flag)
if __name__=='__main__':
    main()
