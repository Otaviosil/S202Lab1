import pymongo
from helper.writeAJson import writeAJson

class ProductAnalyzer:
    def __init__(self, database: str, collection: str):
        self.connectionString = "mongodb://localhost:27017"
        self.client = pymongo.MongoClient(self.connectionString)
        self.db = self.client[database]
        self.collection = self.db[collection]

    def total_vendas_por_dia(self):
        """
        Retorna o total de vendas por dia.
        """
        pipeline = [
            {
                "$group": {
                    "_id": "$data_compra",
                    "total_vendas": {
                        "$sum": {
                            "$sum": {
                                "$map": {
                                    "input": "$produtos",
                                    "as": "produto",
                                    "in": {"$multiply": ["$$produto.quantidade", "$$produto.preco"]}
                                }
                            }
                        }
                    }
                }
            },
            {"$sort": {"_id": 1}}  # Ordena por data
        ]
        resultado = list(self.collection.aggregate(pipeline))
        writeAJson(resultado, "total_vendas_por_dia")
        return resultado

    def produto_mais_vendido(self):
        """
        Retorna o produto mais vendido em todas as compras.
        """
        pipeline = [
            {
                "$unwind": "$produtos"
            },
            {
                "$group": {
                    "_id": "$produtos.descricao",
                    "total_vendas": {
                        "$sum": "$produtos.quantidade"
                    }
                }
            },
            {
                "$sort": {"total_vendas": -1}
            },
            {
                "$limit": 1
            }
        ]
        resultado = list(self.collection.aggregate(pipeline))
        writeAJson(resultado, "produto_mais_vendido")
        return resultado

    def cliente_que_mais_gastou(self):
        """
        Encontra o cliente que mais gastou em uma única compra.
        """
        pipeline = [
            {
                "$project": {
                    "cliente_id": "$cliente_id",
                    "total_gasto": {
                        "$sum": {
                            "$map": {
                                "input": "$produtos",
                                "as": "produto",
                                "in": {"$multiply": ["$$produto.quantidade", "$$produto.preco"]}
                            }
                        }
                    }
                }
            },
            {
                "$sort": {"total_gasto": -1}
            },
            {
                "$limit": 1
            }
        ]
        resultado = list(self.collection.aggregate(pipeline))
        writeAJson(resultado, "cliente_que_mais_gastou")
        return resultado

    def produtos_vendidos_acima_de_um(self):
        """
        Lista todos os produtos que tiveram uma quantidade vendida acima de 1 unidade.
        """
        pipeline = [
            {
                "$unwind": "$produtos"
            },
            {
                "$match": {
                    "$expr": {"$gt": ["$produtos.quantidade", 1]}
                }
            },
            {
                "$group": {
                    "_id": "$produtos.descricao",
                    "total_vendas": {
                        "$sum": "$produtos.quantidade"
                    }
                }
            }
        ]
        resultado = list(self.collection.aggregate(pipeline))
        writeAJson(resultado, "produtos_vendidos_acima_de_um")
        return resultado