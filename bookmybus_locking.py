from threading import *

class BookMyBus:
    def __init__(self,availableSeats):
        self.availableSeats=availableSeats
        self.l=Lock()

    def buy(self,seatRequest):
        self.l.acquire()
        print(current_thread().getName())
        print("Total seats available:",self.availableSeats)
        if self.availableSeats>=seatRequest:
            print("Confirming a seat")
            print("processing a payment")
            print("printing the ticket")
            self.availableSeats-=seatRequest
        else:
            print("Requested seats are not available")
        self.l.release()

obj = BookMyBus(20)
t1=Thread(target=obj.buy,args=(3,))
t2=Thread(target=obj.buy,args=(4,))
t3=Thread(target=obj.buy,args=(15,))
t1.start()
t2.start()
t3.start()