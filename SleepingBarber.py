from threading import Thread, Condition, Event
import time, random

condition = Condition()

customers = 0
barbers = 3
numberOfSeats = 15

class BarberShop:
    customers = []

    def __init__(self, barber, numberOfSeats):
        self.barber = barber
        self.barber1 = barber1
        self.barber2 = barber2
        self.numberOfSeats = numberOfSeats

    def openShop(self):
        print 'Barber shop is opening'
        workingThread = Thread(target = self.barberWorking)
        workingThread.start()

    def barberWorking(self):
        while True:
            condition.acquire()

            if len(self.customers) > 0:
                c = self.customers[0]
                c1 = self.customers[1]
                c2 = self.customers[2]
                del self.customers[0]
                del self.customers[1]
                del self.customers[2]
                condition.release()
                self.barber.cutHair(c)
                self.barber1.cutHair(c1)
                self.barber2.cutHair(c2)
            else:
                condition.release()
                print 'Aaah, all done, going to sleep'
                barber.sleep()
                print 'Barber woke up'
                barber1.sleep()
                print 'Barber1 woke up'
                barber2.sleep()
                print 'Barber2 woke up'
            #except IndexError or SyntaxError:

    def enterBarberShop(self, customer):
        condition.acquire()
        print '>> {0} entered the shop and is looking for a seat\n'.format(customer.name)

        if len(self.customers) == self.numberOfSeats:
            print 'Waiting room is full, {0} is leaving.\n'.format(customer.name)
            condition.release()
        else:
            print '{0} sat down in the waiting room\n'.format(customer.name)
            self.customers.append(c)
            self.customers.append(c1)
            self.customers.append(c2)

            condition.release()
            barber.wakeUp()
            barber1.wakeUp()
            barber2.wakeUp()


class Barber:
    barberWorkingEvent = Event()

    def sleep(self):
        self.barberWorkingEvent.wait()

    def wakeUp(self):
        self.barberWorkingEvent.set()

    def cutHair(self, customer):
        #Set barber as busy
        self.barberWorkingEvent.clear()

        print '{0} is having a haircut from barber\n'.format(customer.name)

        HairCuttingTime = random.randrange(0, 5)
        time.sleep(HairCuttingTime)
        print '{0} is done\n'.format(customer.name)

class Barber1:
    barberWorkingEvent = Event()

    def sleep(self):
        self.barberWorkingEvent.wait()

    def wakeUp(self):
        self.barberWorkingEvent.set()

    def cutHair(self, customer):
        #Set barber as busy
        self.barberWorkingEvent.clear()

        print '{0} is having a haircut from barber1\n'.format(customer.name)

        HairCuttingTime = random.randrange(0, 5)
        time.sleep(HairCuttingTime)
        print '{0} is done\n'.format(customer.name)

class Barber2:
    barberWorkingEvent = Event()

    def sleep(self):
        self.barberWorkingEvent.wait()

    def wakeUp(self):
        self.barberWorkingEvent.set()

    def cutHair(self, customer):
        #Set barber as busy
        self.barberWorkingEvent.clear()

        print '{0} is having a haircut from barber1\n'.format(customer.name)

        HairCuttingTime = random.randrange(0, 5)
        time.sleep(HairCuttingTime)
        print '{0} is done\n'.format(customer.name)


class Customer:
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    newCustomer = []
    newCustomer.append(Customer('Abby'))
    newCustomer.append(Customer('Ben'))
    newCustomer.append(Customer('Chris'))
    newCustomer.append(Customer('Del'))
    newCustomer.append(Customer('Eric'))
    newCustomer.append(Customer('Fred'))
    newCustomer.append(Customer('Guy'))
    newCustomer.append(Customer('High'))
    newCustomer.append(Customer('Ibby'))
    newCustomer.append(Customer('Jen'))
    newCustomer.append(Customer('Khris'))
    newCustomer.append(Customer('Lel'))
    newCustomer.append(Customer('Mric'))
    newCustomer.append(Customer('Ned'))
    newCustomer.append(Customer('Ouy'))
    newCustomer.append(Customer('Pi'))


    barber = Barber()
    barber1 = Barber1()
    barber2 = Barber2()


    barberShop = BarberShop(barber, numberOfSeats)
    barberShop.openShop()


    while len(newCustomer) > 0:
        try:
            c = newCustomer.pop()
            c1 = newCustomer.pop()
            c2 = newCustomer.pop()
            #New customer enters the barbershop
            barberShop.enterBarberShop(c or c1 or c2)
        except IndexError:

            customerInt = random.randrange(0, 5)
            time.sleep(customerInt)
