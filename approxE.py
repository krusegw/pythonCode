
import sys
import math

if __name__ == '__main__':
    TOL = float( sys.argv[1] )
    print('arg',TOL) 
    N = 5
    absErr=10.0
    fileOut = open("approxe.txt","w")
    while N<2000 and absErr>TOL:
        approx = (1.0+1.0/N)**N
        absErr = abs(math.e - approx)
        relErr = absErr/math.e
        #print(N,approx,absErr,relErr)
        outString=str(N)+" "+str(approx)+" "+str(absErr)+" "+str(relErr)+"\n"
        fileOut.write(outString)
        N += 1
    fileOut.close()
