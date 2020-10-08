import sqlite3
import pymongo
import os
from dotenv import load_dotenv
#from pymongo import MongoClient


def connect_to_db(db_name="rpg_db.sqlite3"):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

load_dotenv()

client = pymongo.MongoClient("mongodb+srv://123:123@cluster0.ydtlo.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.test

DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("DB_HOST", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"

print("___")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("___")
print("CLIENT:", type(client), client)

#Can name whatever you want
db = client.test_database

#Can also be named whatever you want like db.blahblah
collection = db.pokemon_test

print("Documents count:", collection.count_documents({}))

#collection.insert_one({
#    "name":"Pikachuuuuu",
#    "level":9000,
#    "exp":3,
#    "hp": 1337,
#    "parents": ["RAICHU", "PIKACHU 2"],
#    "other_attr":{
#        "a":1,
#        "b":2
#    }
#})

print("Documents count:", collection.count_documents({}))
print("Pikachuuuuu count:", collection.count_documents({"name":"Pikachuuuuu"}))

#dir(object) to print out library functions

def select_star_from_table(table):
    t = table[0]
    print(t)
    return f"SELECT * FROM {t}"


select_tables = """
SELECT name FROM sqlite_master WHERE type='table';
"""


if __name__ == "__main__":
    conn = connect_to_db()
    curs = conn.cursor()
    tables = execute_query(curs, select_tables)
    tables = tables[::]

    for table in tables:
        result = execute_query(curs, f"SELECT * FROM {table[0]}")

        q2 = f"SELECT c.name FROM pragma_table_info('{str(table[0])}') c;"
        print(q2)
        table_columns = execute_query(curs, q2)
        collection = db[str(table[0])]
        for val in result:
            dictionary_values = {}
            for i, col in enumerate(table_columns):
                k = val[i]
                dictionary_values[col[0]] = k
                pass
            print(dictionary_values)
            collection.insert_one(dictionary_values)
            
        #collection = db[str(table)]
        #collection.insert_all({result})
    
