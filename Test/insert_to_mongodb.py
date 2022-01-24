import pymongo
import json

cnt = 0
client = pymongo.MongoClient("mongodb://0.0.0.0:27017/")
db = client["movie"]
col = db["movie"]

with open("movies.txt", "r") as fr:
    for i in fr.readlines():
        cnt += 1
        print(json.load(i.rstrip()))
        #col.insert_one(json.dumps(i.rstrip()))

print(cnt)

