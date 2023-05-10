import psycopg2
from psycopg2 import Error

def execute_query(query):
 try:
    connection = psycopg2.connect( user="postgres",
                                   password="1234",
                                   host="localhost",
                                   port= 5433 ,
                                   database="postgres")


    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

 except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
 finally:
      if connection is not None:
        connection.close()

def create_room_table():
    query_room = '''
       CREATE TABLE IF NOT EXISTS Room(
           room_id SERIAL PRIMARY KEY NOT NULL,
           name_room VARCHAR (100) NOT NULL
       )
    '''
    execute_query(query_room)


def create_Clients_table():
    query_Clients = '''
       CREATE TABLE IF NOT EXISTS Clients(
           client_id SERIAL PRIMARY KEY NOT NULL,
           first_name VARCHAR (100) NOT NULL,
           second_name VARCHAR (100) NOT NULL,
           dob TIMESTAMP NOT NULL,
           phone_number SMALLINT NOT NULL,
           email VARCHAR (255) NOT NULL
       )
    '''
    execute_query(query_Clients)
  
def create_booking_table():
    query_booking = '''
        CREATE TABLE IF NOT EXISTS Booking(
            booking_id SERIAL PRIMARY KEY NOT NULL,
            room_id INTEGER,
            client_id INTEGER,
            date_of_booking TIMESTAMP NOT NULL,
            CONSTRAINT fk_room
                FOREIGN KEY(room_id) 
                REFERENCES Room(room_id),
            CONSTRAINT fk_clients
                FOREIGN KEY(client_id) 
                REFERENCES Clients(client_id)
        )
    '''
    execute_query(query_booking)


create_room_table()
create_Clients_table()
create_booking_table()