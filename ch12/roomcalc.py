##  simple application of class
#   $author: Ming
#   $date:   Jan. 11 2015

class HotelRoomCalc(object):
    '''Hotel room rate calculator'''

    def __init__(self, rt, sales=0.085, rm=0.1):
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt

    def calcTotal(self, days = 1):
        daily = round((self.roomRate * (1 + self.roomTax + self.salesTax)), 2)
        return float(days)*daily

def Main():
    sfo = HotelRoomCalc(299)
    print 'normal house cost: ', sfo.calcTotal()

    sea = HotelRoomCalc(399, 0.045, 0.08)
    print 'sea house cost: ', sea.calcTotal()

if __name__ == '__main__' : Main()
