import threading
class TicketBooking:
    def __init__(self,available_ticket):
        self.available_ticket=available_ticket
    def book_ticket(self,name,number_of_ticket):
        print(f'Available tickets are {self.available_ticket}.')
        if self.available_ticket>=number_of_ticket:
            print(f'{name} is booking {number_of_ticket} ticket(s).')
            self.available_ticket-=number_of_ticket
            print(f'Booking of {number_of_ticket} ticket(s) by {name} is done.')
        else:
            print(f'Sorry,{name}!It is not available.')
ticket_booking=TicketBooking(10)
t1=threading.Thread(target=ticket_booking.book_ticket,args=('Riazul',4))
t2=threading.Thread(target=ticket_booking.book_ticket,args=('Pallab',3))
t3=threading.Thread(target=ticket_booking.book_ticket,args=('Aryama',1))
t4=threading.Thread(target=ticket_booking.book_ticket,args=('Arunodaya',2))
t5=threading.Thread(target=ticket_booking.book_ticket,args=('Aniket',2))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()