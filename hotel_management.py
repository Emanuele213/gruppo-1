import psycopg2
from psycopg2 import Error

def execute_query (query):
 try:
    connection = psycopg2.connect(user="unicorn_user",
                                   password="magical_password",
                                   host="127.0.0.1",
                                   port="5433",
                                   database="training")


    cursor = connection.cursor()
    cursor.execute(query)
    record = cursor.fetchall()
    return record

 except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
 finally:
      if connection is not None:
        connection.close()

class Clients:
    def __init__(self,first_name:str,second_name:str,dob,phone_number:int,email:str ):
        self.first_name=first_name
        self.second_name=second_name
        self.dob=dob
        self.phone_number=phone_number
        self.email=email


class ClientsGateway:
    def insert_client(self, client:Clients):
        element = (client.first_name, client.second_name, client.dob,client.phone_number,client.email)
        insert_query = '''INSERT INTO Clients (first_name,second_name,dob,phone_number,email)  
                          VALUES(%s,%s,%s,%s,%s)''' % element
        execute_query(insert_query)
        
    def create_client(self):
        i = input("inserisci valori first_name,second_name,dob,phone_number,email separati da virgola ")
        elem=i.split(",")
        c=Clients(*elem)
        self.insert_client(c)
    

#aggiungere controlli input
    def set_client(self, client_id):
       while True:
           insert_query = "SELECT * from Clients WHERE client_id=" + client_id
           print(execute_query(insert_query))
           campo_modifica = input(" inserisci nome colonna da modificare")
           modifica = input(" inserisci nuovo dato ")
           insert_query = "UPDATE Clients SET " + campo_modifica + " = " + modifica
           execute_query(insert_query)
           new_modifica = input("continuare a modificare Y/N?")
           if (new_modifica == "N"):
                break

    def delete_client(self, client_id):
        insert_query = "DELETE FROM Clients WHERE client_id=+" + client_id
        execute_query(insert_query)
    def get_client(self, client_id):
        insert_query = "SELECT * FROM Clients WHERE client_id=+" + client_id
        print(execute_query(insert_query))


class Room:
    def __init__(self,name_room:str):
        self.name_room=name_room

class roomGateway:
    def insert_room(self, client:Clients):
        element = (Room.name )
        insert_query = '''INSERT INTO Room (name_room)  
                          VALUES(%s)''' % element

        execute_query(insert_query)
        
    def create_room(self):
        i = input("nome Room: ")
        c = Room(i)
        self.insert_room(c)
    

    def set_room(self, room_id):
        while True:
            insert_query = "SELECT * from Room WHERE room_id=" + room_id
            print(execute_query(insert_query))
            campo_modifica = input(" inserisci nome colonna da modificare")
            modifica = input(" inserisci nuovo dato ")
            insert_query = "UPDATE Room SET " + campo_modifica + " = " + modifica
            execute_query(insert_query)
            new_modifica = input("continuare a modificare Y/N?")
            if (new_modifica == "N"):
                break

    def delete_room(self, room_id):
        insert_query = "DELETE FROM Room WHERE room_id=+" + room_id
        execute_query(insert_query)
    def get_room(self,room_id):
        insert_query = "SELECT * FROM Room WHERE room_id=+" + room_id
        print(execute_query(insert_query))
class Booking:
    def __init__(self,room_id,client_id,date_of_booking):
        self.room_id=room_id
        self.client_id=client_id
        self.date_of_booking=date_of_booking

class BookingGateway():
    def insert_Booking(self, booking: Booking):
        element = (booking.room_id,booking.client_id,booking.date_of_booking)
        insert_query = '''INSERT INTO Booking (name)  
                          VALUES(%s,%s,%s)''' % element

        execute_query(insert_query)

    def create_Booking(self):
        i = input("Inserisci dati room_id,client_id,date_of_booking (separati da virgola) ")
        elem = i.split(",")
        b = Booking(*elem)
        self.insert_Booking(b)


    def set_Booking(self, booking_id):
        while True:
            insert_query = "SELECT * from Booking WHERE booking_id=" + booking_id
            print(execute_query(insert_query))
            campo_modifica = input(" inserisci nome colonna da modificare")
            modifica = input(" inserisci nuovo dato ")
            insert_query = "UPDATE Booking SET " + campo_modifica + " = " + modifica
            execute_query(insert_query)
            new_modifica = input("continuare a modificare Y/N?")
            if (new_modifica == "N"):
                break

    def delete_Booking(self, booking_id):
        insert_query = "DELETE FROM Booking WHERE booking_id=+" + booking_id
        execute_query(insert_query)

    def get_Booking(self, booking_id):
        insert_query = '''SELECT first_name.Client,name_room.Room,date_of_booking.Booking
                           FROM Booking b
                            INNER JOIN Room r ON b.room_id=r.room_id
                            INNER JOIN Client c ON c.client_id=c.client_id
                            WHERE booking_id=''' + booking_id
        print(execute_query(insert_query))
        
class Management():
   pass