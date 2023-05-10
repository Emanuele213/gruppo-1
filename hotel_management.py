import psycopg2
from psycopg2 import Error

def execute_query (query):
 try:
    connection = psycopg2.connect( user="postgres",
                                   password="1234",
                                   host="localhost",
                                   port = 5433,
                                   database="postgres")


    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    
    if 'INSERT' not in query or 'DELETE' not in query:
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
    def create_client(self):
        i = input("inserisci valori first_name,second_name,dob,phone_number,email separati da virgola ")
        elem=i.split(",")
        c=Clients(*elem)
        self.insert_client(c)
    def insert_client(self, client:Clients):
        element = (client.first_name, client.second_name, client.dob,client.phone_number,client.email)
        insert_query = '''INSERT INTO Clients (first_name,second_name,dob,phone_number,email)  
                          VALUES('%s','%s','%s','%s','%s')''' % element
        execute_query(insert_query)
        

    
    def all_client(self):
        insert_query = "SELECT * FROM Clients"
        print(execute_query(insert_query))

#aggiungere controlli input
    def set_client(self):
        client_id = int(input("Inserisci l'id"))
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

    def delete_client(self):
        client_id = int(input("Inserisci l'id"))
        insert_query = "DELETE FROM Clients WHERE client_id=+" + client_id
        execute_query(insert_query)
        
    def get_client(self):
        client_id = int(input("Inserisci l'id"))
        insert_query = "SELECT * FROM Clients WHERE client_id=+" + client_id
        print(execute_query(insert_query))


class Room:
    def __init__(self,name_room:str):
        self.name_room=name_room

class roomGateway:
    def create_room(self):
        i = input("nome Room: ")
        r = Room(i)
        self.insert_room(r)
    def insert_room(self, room:Room):
        element = (room.name_room)
        insert_query = '''INSERT INTO Room (name_room)  
                                          VALUES('%s')''' %element

        execute_query(insert_query)


    def set_room(self):
        room_id = input("Inserisci l'id: ")
        while True:
            insert_query = "SELECT * from Room WHERE room_id=" + room_id
            print(execute_query(insert_query))
            campo_modifica = input(" inserisci nome colonna da modificare: ")
            modifica = input(" inserisci nuovo dato: ")
            insert_query = "UPDATE Room SET " + campo_modifica + " = " + "'%s'" %modifica
            execute_query(insert_query)
            new_modifica = input("continuare a modificare Y/N?")
            if (new_modifica == "N"):
                break

    def delete_room(self):
        room_id = input("Inserisci l'id: ")
        insert_query = "DELETE FROM Room WHERE room_id=+" + room_id
        execute_query(insert_query)
        
    def get_room(self):
        room_id = input("Inserisci l'id: ")
        insert_query = "SELECT * FROM Room WHERE room_id=+" + str(room_id)
        print(execute_query(insert_query))
        
    def all_room(self):
        insert_query = "SELECT * FROM Room"
        print(execute_query(insert_query))
        
class Booking:
    def __init__(self,room_id,client_id,date_of_booking):
        self.room_id=room_id
        self.client_id=client_id
        self.date_of_booking=date_of_booking

class BookingGateway():
    def insert_Booking(self, booking: Booking):
        element = (booking.client_id,booking.room_id,booking.date_of_booking)
        insert_query = '''INSERT INTO Booking (client_id,room_id,date_of_booking)  
                          VALUES('%s','%s','%s')''' % element

        execute_query(insert_query)

    def create_Booking(self):
        i = input("Inserisci dati room_id,client_id,date_of_booking (separati da virgola) ")
        elem = i.split(",")
        b = Booking(*elem)
        self.insert_Booking(b)

    def all_booking():
        insert_query = "SELECT * FROM Booking"
        print(execute_query(insert_query))
        
    def set_Booking(self):
        booking_id = input("inserisci il booking id: ")
        while True:
            insert_query = "SELECT * from Booking WHERE booking_id=" + booking_id
            print(execute_query(insert_query))
            campo_modifica = input(" inserisci nome colonna da modificare: ")
            modifica = input(" inserisci nuovo dato: ")
            insert_query = "UPDATE Booking SET " + campo_modifica + " = " + modifica
            execute_query(insert_query)
            new_modifica = input("continuare a modificare Y/N?")
            if (new_modifica == "N"):
                break

    def delete_Booking(self):
        booking_id = input("inserisci il booking id: ")
        insert_query = "DELETE FROM Booking WHERE booking_id=" + booking_id
        execute_query(insert_query)

    def get_Booking(self):
        booking_id = input("inserisci il booking id: ")
        insert_query = '''SELECT first_name.Client,name_room.Room,date_of_booking.Booking
                           FROM Booking b
                            INNER JOIN Room r ON b.room_id=r.room_id
                            INNER JOIN Client c ON c.client_id=c.client_id
                            WHERE booking_id=''' + booking_id
        print(execute_query(insert_query))
        
class Management():
   pass

def menu():
    while True:
        print("\nScegli una delle seguenti opzioni per modificare: ")
        print("Hotel Manager")
        
        print("\nGestione Stanze")
                
        print("\nGestione Cliente")
        
        print("\nGestione Booking")
        
        choice = input("Inserisci opzione scelta: ")
        while True:
            if choice == "Hotel Manager":
                print("1 - Crea stanza")
                print("2 - Visualizza stanze")
                print("3 - Crea Persona")
                print("4 - Visualiuzza Persone")
                print("5 - Crea booking")
                print("6 - Visualizza Booking")
                print("7 - Esci")
                choiceHotel = int(input("Scegli l'opzione con un numero: "))
                if choiceHotel == 1:
                    roomGateway().create_room()
                elif choiceHotel == 2:
                    roomGateway().all_room()
                elif choiceHotel == 3:
                    ClientsGateway().create_client()
                elif choiceHotel == 4:
                    ClientsGateway().all_client()
                elif choiceHotel == 5:
                    BookingGateway().create_Booking()
                elif choiceHotel == 6:
                    BookingGateway().all_booking()
                elif choiceHotel == 7:
                    break
            elif choice == "Stanze":
                print("1 - Aggiorna stanza")
                print("2 - Elimina Stanza")
                print("3 - Ricerca")
                print("4 - Esci")
                
                choiceRoom = int(input("Scegli l'opzione con un numero: "))
                
                if choiceRoom == 1:
                    roomGateway().set_room()
                elif choiceRoom == 2:
                      roomGateway().delete_room()
                elif choiceRoom == 3:
                      roomGateway().get_room()
                elif choiceRoom == 4:
                    break
            elif choice == "Cliente":
                print("1 - Aggiorna cliente")
                print("2 - Elimina cliente")
                print("3 - Ricerca")
                print("4 - Esci")
            
                choiceClient = int(input("Scegli l'opzione con un numero: "))
                if choiceClient == 1:
                    ClientsGateway().set_client()
                elif choiceClient == 2:
                    ClientsGateway().delete_client
                elif choiceClient == 3:
                    ClientsGateway().get_client()
                elif choiceClient == 4:
                    break
                
            elif choice == "Booking":
                print("1 - Aggiorna booking")
                print("2 - Elimina booking")
                print("3 - Ricerca")
                print("4 - Esci")
                choiceBooking = int(input("Scegli l'opzione con un numero: "))
                if choiceBooking == 1:
                    BookingGateway().set_Booking()
                elif choiceBooking == 2:
                    BookingGateway().delete_Booking()
                elif choiceBooking == 3:
                    BookingGateway().get_Booking()
                elif choiceBooking == 4:
                    break
            else:
                print("\nScelta non valida. Riprova.")
                break



menu()