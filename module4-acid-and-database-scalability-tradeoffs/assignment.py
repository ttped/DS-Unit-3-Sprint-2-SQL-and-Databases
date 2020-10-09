import pymongo
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

client = pymongo.MongoClient("mongodb+srv://123:123@cluster0.ydtlo.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.test

DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("DB_HOST", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"

client = pymongo.MongoClient(connection_uri)

#Can name whatever you want
db = client.test_database

#df = pd.read_csv('titanic.csv')
#df['Survived'] = df['Survived'].map(lambda x: True if x == 1 else False)

#collection = db.titanic
#collection.insert_many(df.to_dict('records'))


x = db.titanic.find( {} )

for doc in x:
    print(doc)
