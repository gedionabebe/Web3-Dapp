from pymongo import MongoClient

client = MongoClient('localhost', 27017)
database = client.web3
trainees = database.trainess
admins = database.admins
first = {"name":"init","description":"database init"}
trainees.insert_one(first).inserted_id
admins.insert_one(first).inserted_id