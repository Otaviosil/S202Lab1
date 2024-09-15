from database import Database


class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, motorista):
        return self.db.collection.insert_one(motorista)

    def read_motorista(self, query):
        return self.db.collection.find_one(query)

    def update_motorista(self, query, new_values):
        return self.db.collection.update_one(query, {"$set": new_values})

    def delete_motorista(self, query):
        return self.db.collection.delete_one(query)