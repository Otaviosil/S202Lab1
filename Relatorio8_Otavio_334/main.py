from database import Database
from game_database import GameDatabase

db = Database("bolt://44.202.183.24:7687", "neo4j", "rescuers-stairs-combinations")
db.drop_all()

game_db = GameDatabase(db)

game_db.create_player("p1", "João")
game_db.create_player("p2", "Maria")
game_db.create_player("p3", "José")

game_db.create_match("m1", ["p1", "p2"], {"p1": 10, "p2": 5})
game_db.create_match("m2", ["p2", "p3"], {"p2": 7, "p3": 3})
game_db.create_match("m3", ["p1", "p3"], {"p1": 2, "p3": 8})

game_db.update_player("p1", "Pedro")

game_db.delete_match("m2")

print("Jogadores:")
print(game_db.get_players())
print("Partida m1:")
print(game_db.get_match("m1"))
print("Partidas de João:")
print(game_db.get_player_matches("p1"))

db.close()