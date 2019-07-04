import random as rand
import time
import argparse
import math

def no_neighbors(amt,options,bounds,iter,cur):
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
                    num2 = num+1
                    num3 = num-1
                    while ((num == num2) or (num == num3)):
                        num = rand.choice(options)
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
            print("Created {} coordinates to this point".fotmat(iter))
            return

class dim2:
    def __init__(self,options,bounds,cur,amt,flag):
        self.options = options
        self.bounds = bounds
        self.cur = cur
        self.amt = amt
        self.flag = flag
        self.iter = 0

    def halfway(self,a,b):
        return [(a[0]+b[0])/2, (a[1]+b[1])/2]

    def random_numbers(self):
        if iter == 0:
            self.iter += 1
        elif iter == 1:
            self.cur = self.halfway(self.cur, self.bounds[rand.choice(self.options[1:])])
            self.iter += 1
        else:
            self.cur = self.halfway(self.cur, self.bounds[rand.choice(self.options)])
            self.iter += 1

    def no_prev_vertex(self):
        iter = 0
        file = open('fractaldata.csv', 'a')
        file.write('x,y')
        file.write('\n')
        try:
            while iter < int(self.amt):
                if iter == 0:
                    file.write(str(self.cur[0])+','+str(self.cur[1]))
                    file.write('\n')
                    iter += 1
                elif iter == 1:
                    num = rand.choice(self.options[1:])
                    vertex = self.bounds[rand.choice(self.options[1:])]
                    cur = halfway(self.cur,self.vertex )
                    file.write(str(self.cur[0])+','+str(self.cur[1]))
                    file.write('\n')
                    iter += 1
                    prev = self.cur
                else:
                    num1 = num
                    options.remove(num)
                    num = rand.choice(self.options)
                    options.append(num1)
                    vertex = bounds[num]
                    cur = halfway(self.cur, vertex)
                    file.write(str(self.cur[0])+','+str(self.cur[1]))
                    file.write('\n')
                    iter += 1
                    prev = self.cur
            file.close()
            print("Done")
            return
        except KeyboardInterrupt:
            print("Created {} coordinates to this point".fotmat(iter))
            return

    def numbers_to_file(self):
        iter = 0
        if self.flag == 1:
            self.no_prev_vertex()
        elif self.flag == 2:
            return
            #no_neighbors(self.amt,options,bounds,iter,cur)
        else:
            file = open('fractaldata.csv', 'a')
            file.write('x,y')
            file.write('\n')
            try:
                while self.iter < int(self.amt):
                    self.random_numbers()
                    file.write(str(self.cur[0])+','+str(self.cur[1]))
                    file.write('\n')
                file.close()
                print("Done")
                return
            except KeyboardInterrupt:
                print("Stopped at: ",self.iter)
        return

class dim3:
    def __init__(self,options,bounds,cur,amt,flag):
        self.options = options
        self.bounds = bounds
        self.cur = cur
        self.amt = amt
        self.flag = flag
        self.iter = 0

    def halfway(self,a,b):
        return ((a[0]+b[0])/2,(a[1]+b[1])/2,(a[2]+b[2])/2)

    def random_numbers(self):
        if iter == 0:
            self.iter += 1
        elif iter == 1:
            self.cur = self.halfway(self.cur, self.bounds[rand.choice(self.options[1:])])
            self.iter += 1
        else:
            self.cur = self.halfway(self.cur, self.bounds[rand.choice(self.options)])
            self.iter += 1

    def no_prev_vertex(self):
        iter = 0
        file = open('fractaldata.csv', 'a')
        file.write('x,y')
        file.write('\n')
        try:
            while iter < int(self.amt):
                if iter == 0:
                    file.write(str(self.cur[0])+','+str(self.cur[1]))
                    file.write('\n')
                    iter += 1
                elif iter == 1:
                    num = rand.choice(self.options[1:])
                    vertex = self.bounds[rand.choice(self.options[1:])]
                    cur = halfway(self.cur,self.vertex )
                    file.write(str(self.cur[0])+','+str(self.cur[1])+','+str(self.cur[2]))
                    file.write('\n')
                    iter += 1
                    prev = self.cur
                else:
                    num1 = num
                    options.remove(num)
                    num = rand.choice(self.options)
                    options.append(num1)
                    vertex = bounds[num]
                    cur = halfway(self.cur, vertex)
                    file.write(str(self.cur[0])+','+str(self.cur[1])+','+str(self.cur[2]))
                    file.write('\n')
                    iter += 1
                    prev = self.cur
            file.close()
            print("Done")
            return

        except KeyboardInterrupt:
            print("Created {} coordinates to this point".fotmat(iter))
            return

    def numbers_to_file(self):

        iter = 0
        if self.flag == 1:
            self.no_prev_vertex()
        elif self.flag == 2:
            return
            #no_neighbors(self.amt,options,bounds,iter,cur)
        else:
            file = open('fractaldata.csv', 'a')
            file.write('x,y,z')
            file.write('\n')
            try:
                while self.iter < int(self.amt):
                    self.random_numbers()
                    file.write(str(self.cur[0])+','+ str(self.cur[1])+','+str(self.cur[2]))
                    file.write('\n')
                file.close()
                print("Done")
                return
            except KeyboardInterrupt:
                print("Stopped at: ",self.iter)
        return

def main():
    flag = 0
    threeD = 0
    parser = argparse.ArgumentParser("Description = Chaos Game Fractals!")
    g = parser.add_mutually_exclusive_group()
    g.add_argument('-n', '--npv', action = 'store_true', help = 'Next vertex cannot be the previous vertex')
    g.add_argument('-b','--neighbor', action = 'store_true',help = 'Cannon move to neighbor vertices')
    g2 = parser.add_mutually_exclusive_group()
    g.add_argument('-td', '--dim3', action = 'store_true', help = '3d fractal plot')
    args = parser.parse_args()
    if args.npv: flag = 1
    if args.neighbor: flag = 2
    if args.dim3: threeD = 1

    '''2D POLYGONS'''
    '''Triangle'''
    # bounds = [(0,0),(1,0),(.5,1)]
    # cur = [0,0]
    '''Pentagon'''
    # bounds = [(.2,0),(.8,0),(1,.6),(.5,1),(0,.6)]
    # cur = [.2,0]
    '''Square '''
    # bounds = [(0,0),(0,1),(1,0),(1,1)]
    # cur = [0,0]
    '''Diamond'''
    # bounds = [(.5,0),(1,.5),(0,.5),(.5,1)]
    # cur = [.5,0]
    '''Spear'''
    # bounds = [(.5,0),(1,.2),(0,.2),(.5,1)]
    # cur = [.5,0]
    '''Star'''
    # bounds = [(.33,0),(.66,0),(1,.66),(0,.66),(.5,1)]
    # cur = [.33,0]
    ''''''
    # bounds = [(.4,0),(.6,0),(0,.6),(0,.4),(1,.4),(1,.6),(.4,1),(.6,1)]
    # cur = [(.4,0)
    '''3D'''
    '''TRIANGULAR PRISM'''
    bounds = [(0,0,0),(1,0,0),(1,0,1),(0,0,1),(.5,1,.5)]
    cur = [0,0,0]

    options = []
    for i in range(len(bounds)):
        options.append(i)
    file = open('fractaldata.csv', 'w').close()
    amt = input("How many datapoints: ")

    if threeD:
        dim3(options,bounds,cur,amt,flag).numbers_to_file()
    else: dim2(options,bounds,cur,amt,flag).numbers_to_file()

    # numbers_to_file(options,bounds,amt,flag)
if __name__=='__main__':
    main()
