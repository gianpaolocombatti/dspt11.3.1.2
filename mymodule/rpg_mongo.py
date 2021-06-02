import pymongo
import sqlite3
import os

mongo_pass = os.environ['MONGO_PASS']


mongo_client = pymongo.MongoClient("mongodb+srv://gianpaolocombatti:{}@cluster0.sz1au.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".format(mongo_pass))

db = mongo_client.test

sqlite_conn = sqlite3.connect('/Users/gianpaolocombatti/dspt11.3.1.2/rpg_db.sqlite3')

sqlite_cursor = sqlite_conn.cursor()
collection = mongo_client.myFirstDatabase['rpg_data']
collection.drop({})

character_query = """SELECT * FROM charactercreator_character;"""

item_query = """SELECT * FROM armory_item left armory_weapon on armory_item.item_id = armory_weapon.item_pte_id;"""