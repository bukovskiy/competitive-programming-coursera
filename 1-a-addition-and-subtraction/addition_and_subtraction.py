#python3

import sys
import math

def check(x,y,z):

    d = x-y
    var1, var2 = 0, 0
    if(z==x):
        return 1
    if(z==(x-y)):
        return 2
    if(x==y):
        return -1
    if((z-(x-d))%d==0 and (z-(x-d))!=0):
        var1=math.fabs(((z-(x-d))/d)*2)-1
        print(math.fabs(((z-(x-d))/d)*2)-1)
    if(z%(x-y)==0 and z/(x-y)>0):
        var2 = (z/(x-y))*2
#        print((z/(x-y))*2)

    if(var1 and var2):
        return min([var1, var2])
    elif(var1 and not var2):
        return var1
    elif(var2 and not var1):
        return var2
    elif(not var1 and not var2):
        return -1



def main():
    x, y, z = map(int, input().split())
    
    print(int(check(x,y,z)))

if __name__ == '__main__':
    main()

