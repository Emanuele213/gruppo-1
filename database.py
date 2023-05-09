import psycopg2


def create_room_table():
    query_room = '''
       CREATE TABLE IF NOT EXISTS Room(
           room_id SERIAL PRIMARY KEY NOT NULL,
           name_room VARCHAR (100) NOT NULL
       )
    '''
    cursor = connection.cursor()
    cursor.execute(query_room)
    connection.commit()


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
    cursor = connection.cursor()
    cursor.execute(query_Clients)
    connection.commit()
  
def create_booking_table():
    '''PRIMARY KEY (client_id, room_id),
     FOREIGN KEY (client_id)
         REFERENCES Clients (client_id),
     FOREIGN KEY (room_id)
         REFERENCES Room (room_id)'''

    query_booking = '''
       CREATE TABLE IF NOT EXISTS Booking(
           booking_id SERIAL PRIMARY KEY NOT NULL,
           room_id INTEGER ,
           client_id INTEGER,
           date_of_booking TIMESTAMP NOT NULL
           CONSTRAINT fk_room
             FOREIGN KEY(room_id) 
             REFERENCES Room(room_id) 
           CONSTRAINT fk_clients
             FOREIGN KEY(client_id) 
             REFERENCES Client(client_id) 
       )
    '''
    cursor = connection.cursor()
    cursor.execute(query_booking)
    connection.commit()


try:
    connection = psycopg2.connect(user="unicorn_user",
                                  password="magical_password",
                                  host="127.0.0.1",
                                  port="5433",
                                  database="training")
    create_booking_table()
    create_room_table()
    create_booking_table()


except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")