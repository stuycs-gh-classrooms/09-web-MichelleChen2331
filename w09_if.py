def max3(a, b, c):
    if ( a > b and a > c):
        return(a)
    elif ( b > a and b > c):
        return(b)
    else: return(c)

import math

def distance(x0, y0, x1, y1):
    result = math.sqrt( (x1 - x0)**2 + (y1 - y0)**2)
    return result

def closer_point(x0, y0, x1, y1, x2, y2):
    a = (distance(x0, y0, x2, y2))
    b = (distance(x1, y1, x2, y2))
    if ( a > b ):
        print (x0, y0, "is closer to" + x2, y2)
    elif ( b > a):
        print (x1, y1, "is closer to", x2, y2)
    else: print (x0, y0,  "and", x1, y1, "are the same distance from" + x2, y2)

def is_leap_year(y):
    if ((y % 400 == 0) or (y % 100 != 0) and (y % 4 == 0)):
        print (y, "is a leap year")
    else:
        print (y, "is not a leap year")

is_leap_year(2024)
is_leap_year(2021)