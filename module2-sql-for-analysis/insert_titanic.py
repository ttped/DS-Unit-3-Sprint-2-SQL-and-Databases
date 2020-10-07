import psycopg2
import os
from dotenv import load_dotenv
import pandas as pd
from psycopg2.extras import execute_values
import sql

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                              password=DB_PASSWORD, host=DB_HOST)

print("Connection", connection)

cursor = connection.cursor()

df = pd.read_csv('titanic.csv')

df['Survived'] = df['Survived'].map(lambda x: True if x == 1 else False)

#df.to_sql('titanic_passengers', connection, schema='postgresql')

df_tuple = [tuple(x) for x in df.values]

#insert_query = "INSERT INTO titanic_passengers (survived, pclass, name, sex, age, sibling_spouse_aboard, parent_children_aboard, fare) VALUES %s"
#execute_values(cursor, insert_query, df_tuple)

query = """
    SELECT count(survived)
    FROM titanic_passengers
    WHERE survived = TRUE
    """

cursor.execute(query)

result = cursor.fetchall()
print("Number of passengers that survived:", result)

query = """
    SELECT count(survived)
    FROM titanic_passengers
    WHERE survived = FALSE
    """

cursor.execute(query)

result = cursor.fetchall()
print("Number of passengers that died:", result)

query = """
    SELECT avg(age)
    FROM titanic_passengers
    """

cursor.execute(query)

result = cursor.fetchall()
print("Average age", result)


connection.commit()
cursor.close()
