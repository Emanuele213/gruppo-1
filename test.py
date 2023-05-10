import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="postgres",
                                  password="1234",
                                  host="localhost",
                                  port=5433,
                                  database="postgres")

    cursor = connection.cursor()
    query_room = '''
           CREATE TABLE IF NOT EXISTS Room(
               room_id SERIAL PRIMARY KEY NOT NULL,
               name_room VARCHAR (100) NOT NULL
           )
        '''
    cursor.execute(query_room)
    connection.commit()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection is not None:
        connection.close()