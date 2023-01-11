
import random
import math

def distance(x,y):
    return math.sqrt(x**2+y**2)

if __name__ == '__main__':
    #N = int( input('Enter the number of points N, to simulate: ') )
    for n in range(1,8):
        N = 10**n
        inCircle = 0
        for i in range(N):
          x = random.random()
          y = random.random()
          if distance(x,y)<=1.0:
             inCircle +=1
         # print(x,y,distance(x,y),inCircle)
        PiEstimate = 4.0*inCircle/N
        absErr = abs(PiEstimate-math.pi)
        relErr = absErr/math.pi
        print(N,PiEstimate,absErr,relErr)

