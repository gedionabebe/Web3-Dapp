from pymongo import MongoClient

client = MongoClient('localhost', 27017)
database = client.web3
trainees = database.trainess
first = {"name":"init","description":"database init"}
trainees.insert_one(first).inserted_id