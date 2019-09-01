import time
import sys
import math
print("this programs let you find area of any triangle of which you khow three sides")
time.sleep(.2)
sidea = int(input("please wirte side a: "))
time.sleep(.5)
sideb = int(input("please write side b: "))
time.sleep(.5)
sidec = int(input("please write side c: "))
time.sleep(.7)
string = ('....>>>>>> putting herons formula...got it!')
for char in string:
        time.sleep(0.10)
        sys.stdout.write(char)
        sys.stdout.flush()

def heron_area(x,y,z):
    s = (x/2 + y/2 + z/2 )
    areax = s*(s-x)*(s-y)*(s-z)
    areay = math.sqrt(areax)
    print("s = ",s,"so..area =","<<<<",areay,">>>>")

heron_area(sidea,sideb,sidec)
    
    
