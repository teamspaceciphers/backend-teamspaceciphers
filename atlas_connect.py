from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# uri = "mongodb+srv://devanshu:Rathod%40pace01@cluster0.lvq61.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
uri = "mongodb://ronitrathod:Rathod%40pace01@localhost:27017/admin"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)