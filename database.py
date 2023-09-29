from pymongo import MongoClient


def get_database():
    CONNECTION_STRING = "mongodb+srv://z4kvt4:06041998Aa@miclusterappnode.cd40k.mongodb.net/melcosur_app"
    client = MongoClient(CONNECTION_STRING)

    return client["melcosur_app"]
