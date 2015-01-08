from random import *
from time import *
date1 = (2008, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = mktime(date1)
date2 = (2009, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = mktime(date2)

def print_time():
    random_time = uniform(time1, time2)
    print asctime(localtime(random_time))

if __name__ == '__main__' : print_time()

