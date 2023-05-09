import psycopg2

def create_room_table():
    query_room = '''
       CREATE TABLE Room(
           room_id SERIAL PRIMARY KEY NOT NULL,
           name VARCHAR (100) NOT NULL
       )
    '''
    
def create_booking_table():
    query_booking = '''
       CREATE TABLE People(
           people_id SERIAL PRIMARY KEY NOT NULL,
           first_name VARCHAR (100) NOT NULL,
           second_name VARCHAR (100) NOT NULL,
           dob TIMESTAMP NOT NULL,
           phone_number SMALLINT NOT NULL,
           email VARCHAR (255) NOT NULL
       )
  '''
  
def create_booking_table():
    query_booking = '''
       CREATE TABLE Booking(
           booking_id SERIAL PRIMARY KEY NOT NULL,
           room_id INTEGER ,
           people_id INTEGER,
           date_of_booking TIMESTAMP NOT NULL
           CONSTRAINT fk_room
             FOREIGN KEY(room_id) 
             REFERENCES Room(room_id) 
           CONSTRAINT fk_people
             FOREIGN KEY(people_id) 
             REFERENCES People(people_id) 
       )
  '''