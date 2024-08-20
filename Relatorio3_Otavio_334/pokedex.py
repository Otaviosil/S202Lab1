from helper.writeAJson import writeAJson
from database import Database

class Pokedex:
    def __init__(self, database: Database):
        self.database = database

    def get_all_pokemons(self):
        try:
            result = list(self.database.collection.find({}))
            writeAJson(result, "all_pokemons")
            return result
        except Exception as e:
            print(e)
            return []

    def get_pokemon_by_name(self, name: str):
        try:
            result = self.database.collection.find_one({"name": name})
            writeAJson(result, f"pokemon_{name}")
            return result
        except Exception as e:
            print(e)
            return None

    def get_pokemons_by_type(self, type: str):
        try:
            result = list(self.database.collection.find({"type": type}))
            writeAJson(result, f"pokemons_type_{type}")
            return result
        except Exception as e:
            print(e)
            return []

    def get_pokemons_with_candy_count(self, candy_count: int):
        try:
            result = list(self.database.collection.find({"candy_count": candy_count}))
            writeAJson(result, f"pokemons_candy_{candy_count}")
            return result
        except Exception as e:
            print(e)
            return []

    def get_pokemons_with_high_spawn_chance(self, spawn_chance_threshold: float):
        try:
            result = list(self.database.collection.find({"spawn_chance": {"$gte": spawn_chance_threshold}}))
            writeAJson(result, f"pokemons_spawn_chance_{spawn_chance_threshold}")
            return result
        except Exception as e:
            print(e)
            return []

db = Database(database="pokedex", collection="pokemons")
pokedex = Pokedex(database=db)

db.resetDatabase()

pokedex.get_all_pokemons()
pokedex.get_pokemon_by_name("Bulbasaur")
pokedex.get_pokemons_by_type("Fire")
pokedex.get_pokemons_with_candy_count(25)
pokedex.get_pokemons_with_high_spawn_chance(0.1)