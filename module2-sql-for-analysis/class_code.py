import psycopg2
import os
from dotenv import load_dotenv
import pandas as pd
from psycopg2.extras import execute_values

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

#print(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST)
#exit()

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                              password=DB_PASSWORD, host=DB_HOST)

print("Connection", connection)

cursor = connection.cursor()

#cursor.execute("SELECT * FROM test_table;")

#result = cursor.fetchall()
#print(result)

#insert_into_test = "INSERT INTO test_table (name) VALUES ('bob')"

#cursor.execute(insert_into_test)

insert_query = "INSERT INTO charactercreator_character (name, level, experience, hp, strength, intelligence, dexterity, wisdom) VALUES %s"
execute_values(cursor, insert_query, [
    ('bob2', 1, 2, 3, 4, 5, 6, 7),
    ('joe2', 2, 3, 4, 4, 5, 6, 7),
    ('jane2', 4, 5, 6, 7, 5, 6, 7)
])

connection.commit()
cursor.close()

'''
insert_query = "INSERT INTO test_table (name) VALUES(%s)"
execute_values(cursor, insert_query, [
    ('bob'),
    ('jane')
])
'''

