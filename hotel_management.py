import psycopg2
from psycopg2 import Error
import pandas as pd
def execute_query(query):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="1234",
            host="localhost",
            port=5433,
            database="postgres")

        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

        if 'SELECT' in query :
           if 'NOT EXISTS' not in query:
            record = cursor.fetchall()
            return record
           else:
               return None
        else:
            return None

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
        i = input("inserisci valori first_name,second_name,dob,phone_number,email separati da virgola = ")
        elem=i.split(",")
        c=Clients(*elem)
        self.insert_client(c)
        print("\nCliente creato")
        
    def insert_client(self, client:Clients):
        element = (client.first_name, client.second_name, client.dob,client.phone_number,client.email)
        insert_query = '''INSERT INTO Clients (first_name,second_name,dob,phone_number,email)  
                          VALUES('%s','%s','%s','%s','%s')''' % element
        execute_query(insert_query)
        

    
    def all_client(self):
        insert_query = "SELECT * FROM Clients"
        print((pd.DataFrame(execute_query(insert_query),columns=("id_client","first_name","second_name","dob","phone_number","email"))).to_string(index=False))

    def set_client(self):
        client_id = input("Inserisci l'id: ")
        while True:
            insert_query = "SELECT * from Clients WHERE client_id=" + client_id
            print((pd.DataFrame(execute_query(insert_query), columns=("client_id", "first_name", "second_name", "dob", "phone_number", "email"))).to_string(index=False))
            campo_modifica = input(" inserisci nome colonna da modificare: ")
            modifica = input(" inserisci nuovo dato: ")
            insert_query = '''UPDATE Clients SET %s ='%s' WHERE client_id=%s'''%(campo_modifica,modifica,str(client_id))
            execute_query(insert_query)
            print("\nCliente modificato")
            new_modifica = input("Continuare a modificare Y/n?")
            if (new_modifica == "n"):
                break

    def delete_client(self):
        client_id = input("Inserisci l'id: ")
        insert_query = "DELETE FROM Clients WHERE client_id=" + client_id
        execute_query(insert_query)
        print("\nCliente eliminato")
        
    def get_client(self):
        client_id = input("Inserisci l'id: ") 
        insert_query = "SELECT * FROM Clients WHERE client_id=" + client_id
        print((pd.DataFrame(execute_query(insert_query),columns=("id_client","first_name","second_name","dob","phone_number","email"))).to_string(index=False))


class Room:
    def __init__(self,name_room:str):
        self.name_room=name_room

class roomGateway:
    def create_room(self):
        i = input("\nNome stanza: ")
        r = Room(i)
        self.insert_room(r)
        print("\nStanza creata")
        
    def insert_room(self, room:Room):
        element = (room.name_room)
        insert_query = '''INSERT INTO Room (name_room)  
                                          VALUES('%s')''' %element

        execute_query(insert_query)


    def set_room(self):
        room_id = input("Inserisci l'id: ")
        while True:
            insert_query = "SELECT * from Room WHERE room_id=" + room_id
            print((pd.DataFrame(execute_query(insert_query),columns=("room_id","name_room"))).to_string(index=False))
            campo_modifica = input(" inserisci nome colonna da modificare: ")
            modifica = input(" inserisci nuovo dato: ")
            insert_query = '''UPDATE Room SET %s ='%s' WHERE room_id=%s'''%(campo_modifica,modifica,str(room_id))
            execute_query(insert_query)
            insert_query ="SELECT * from Room WHERE room_id=" + room_id
            update=execute_query(insert_query)
            print(f"\nStanza modificata {(pd.DataFrame(update,columns=('room_id','name_room'))).to_string(index=False)}")
            new_modifica = input("Continuare a modificare Y/n?")
            if (new_modifica == "n"):
                break

    def delete_room(self):
        room_id = input("Inserisci l'id: ")

        insert_query = '''DELETE FROM Room 
                           WHERE NOT EXISTS( SELECT room_id FROM booking WHERE room_id= %s) AND room_id=%s
                           '''%(room_id,room_id)
        execute_query(insert_query)
        
    def get_room(self):
        room_id = input("Inserisci l'id: ")
        insert_query = "SELECT * FROM Room WHERE room_id=" + str(room_id)
        print((pd.DataFrame(execute_query(insert_query),columns=('room_id','name_room'))).sort_values(by='room_id').to_string(index=False))
        
    def all_room(self):
        insert_query = "SELECT * FROM Room"
        print((pd.DataFrame(execute_query(insert_query),columns=('room_id','name_room'))).sort_values(by='room_id').to_string(index=False))
        
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
        query_test='''SELECT room_id FROM Booking WHERE room_id=%s '''%(elem[0])
        print(execute_query(query_test))
        if len(execute_query(query_test))>0:
           print("Stanza occupata!!!")
        elif len(execute_query('''SELECT client_id FROM Booking WHERE client_id=%s '''%(elem[1])))>0:
            print("Il cliente ha già una camera !!")
        else:
           b = Booking(*elem)
           self.insert_Booking(b)
           print("\nPrenotazione creata")

    def all_booking(self):
        insert_query ='''SELECT c.first_name, r.name_room, b.date_of_booking
                           FROM Booking b
                           INNER JOIN Room r ON b.room_id=r.room_id
                           INNER JOIN Clients c ON c.client_id=b.client_id'''
        print((pd.DataFrame(execute_query(insert_query),columns=('Cliente', 'Stanza', 'date_of_booking'))).to_string(index=False))

    def set_Booking(self):
        booking_id = input("inserisci il booking id: ")
        while True:
            insert_query = "SELECT * from Booking WHERE booking_id=" + booking_id
            print((pd.DataFrame(execute_query(insert_query),columns=('booking_id','room_id','client_id','date_of_booking'))).to_string(index=False))
            campo_modifica = input(" inserisci nome colonna da modificare: ")
            modifica = input(" inserisci nuovo dato: ")
            insert_query = '''UPDATE Booking SET %s ='%s' WHERE  NOT EXISTS( SELECT %s FROM booking WHERE %s= %s) AND booking_id=%s'''%(campo_modifica,modifica,campo_modifica,campo_modifica,modifica,booking_id)
            execute_query(insert_query)
            new_modifica = input("continuare a modificare y/n?")
            if (new_modifica == "n"):
                break

    def delete_Booking(self):
        booking_id = input("inserisci il booking id: ")
        insert_query = "DELETE FROM Booking WHERE booking_id=" + booking_id
        execute_query(insert_query)

    def get_Booking(self):
        booking_id = input("inserisci il booking id: ")
        insert_query = '''SELECT c.first_name, r.name_room, b.date_of_booking
                           FROM Booking b
                           INNER JOIN Room r ON b.room_id=r.room_id
                           INNER JOIN Clients c ON c.client_id=b.client_id
                           WHERE booking_id=''' + booking_id
        print((pd.DataFrame(execute_query(insert_query), columns=('Cliente','Stanza','date_of_booking'))).to_string(index=False))


def menu():
    while True:
        print("\nScegli una delle seguenti opzioni per modificare: ")
        print("1 - Hotel Manager")
        
        print("\n2 - Gestione Stanze")
                
        print("\n3 - Gestione Cliente")
        
        print("\n4 - Gestione Booking")
        
        choice = input("Inserisci opzione scelta: ")
        while True:
            if choice == "Hotel Manager":
                print("\n1 - Crea stanza")
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
                print("\n1 - Aggiorna stanza")
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
                print("\n1 - Aggiorna cliente")
                print("2 - Elimina cliente")
                print("3 - Ricerca")
                print("4 - Esci")
            
                choiceClient = int(input("Scegli l'opzione con un numero: "))
                if choiceClient == 1:
                    ClientsGateway().set_client()
                elif choiceClient == 2:
                    ClientsGateway().delete_client()
                elif choiceClient == 3:
                    ClientsGateway().get_client()
                elif choiceClient == 4:
                    break
                
            elif choice == "Booking":
                print("\n1 - Aggiorna booking")
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