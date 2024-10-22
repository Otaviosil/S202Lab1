from database import Database

class Query:
    def __init__(self):
        self.db = Database("bolt://44.204.237.47", "neo4j", "peas-back-matter")

    def close(self):
        self.db.close()

    def query_1(self):
        query = """
        MATCH (t:Teacher {name: 'Renzo'})
        RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf
        """
        results = self.db.execute_query(query)
        return results

    def query_2(self):
        query = """
        MATCH (t:Teacher)
        WHERE t.name STARTS WITH 'M'
        RETURN t.name AS name, t.cpf AS cpf
        """
        results = self.db.execute_query(query)
        return results

    def query_3(self):
        query = """
        MATCH (c:City)
        RETURN c.name AS name
        """
        results = self.db.execute_query(query)
        return results

    def query_4(self):
        query = """
        MATCH (s:School)
        WHERE s.number >= 150 AND s.number <= 550
        RETURN s.name AS name, s.address AS address, s.number AS number
        """
        results = self.db.execute_query(query)
        return results

    def query_5(self):
        query = """
        MATCH (t:Teacher)
        RETURN MIN(t.ano_nasc) AS oldest_birth_year, MAX(t.ano_nasc) AS youngest_birth_year
        """
        results = self.db.execute_query(query)
        return results

    def query_6(self):
        query = """
        MATCH (c:City)
        RETURN AVG(c.population) AS average_population
        """
        results = self.db.execute_query(query)
        return results

    def query_7(self):
        query = """
        MATCH (c:City {cep: '37540-000'})
        RETURN REPLACE(c.name, 'a', 'A') AS city_name
        """
        results = self.db.execute_query(query)
        return results

    def query_8(self):
        query = """
        MATCH (t:Teacher)
        RETURN SUBSTRING(t.name, 2, 1) AS third_letter
        """
        results = self.db.execute_query(query)
        return results

if __name__ == "__main__":
    query = Query()
    
    print("Query 1:")
    print(query.query_1())
    
    print("Query 2:")
    print(query.query_2())
    
    print("Query 3:")
    print(query.query_3())
    
    print("Query 4:")
    print(query.query_4())
    
    print("Query 5:")
    print(query.query_5())
    
    print("Query 6:")
    print(query.query_6())
    
    print("Query 7:")
    print(query.query_7())
    
    print("Query 8:")
    print(query.query_8())
    
    query.close()