import pymongo

client = pymongo.MongoClient("mongodb+srv://icici11:India123$@cluster0.4nvln5o.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "vikas",
    "email": "vikas@ineuron.ai",
    "surname": "gupta"
}

d = {
    "name": "vikas",
    "email": "vikas@ineuron.ai",
    "surname": "gupta"
}

d = {
    "name": "vikas",
    "email": "vikas@ineuron.ai",
    "surname": "gupta"
}

d = {
    "name": "vikas",
    "email": "vikas@ineuron.ai",
    "surname": "gupta"
}

d = {
    "name": "vikas",
    "email": "vikas@ineuron.ai",
    "surname": "gupta"
}


db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)


