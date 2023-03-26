from database import Database
from WriteAJson import WriteAJson


class ProductAnalyzer:
    def __init__(self, database, collection):

        self.db = Database(database, collection)
    
    
    def venda(self):

        r = self.db.collection.aggregate([
        {"$unwind":"$produtos"},
        {"$group": {"_id": "$data_compra", "Total":{"$sum": "$produtos.quantidade"}}},
        {"$sort": {"Total": -1}}

    ])
        WriteAJson(r, "Venda")


    
    def top_sale(self):

        r2 = self.db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": "$produtos.descricao", "Total": {"$sum": "$produtos.quantidade"}}},
        {"$sort": {"Total": -1}},
        {"$limit": 1}
    ])
        WriteAJson(r2, "Produto mais vendido")


    def top_cliente(self):

        r3 = self.db.collection.aggregate([
        {"$unwind":"$produtos"},
        {"$group":{"_id":"$cliente_id","total":{"$sum":{"$multiply":["$produtos.quantidade","$produtos.preco"]}}}},
        {"$sort":{"total": -1}},
        {"$limit": 1}
    ])
        WriteAJson(r3, "Cliente Premium")

    
    def maisDeUmaVenda(self):

        r4 = self.db.collection.aggregate([
        {"$unwind":"$produtos"},
        {"$match":{"produtos.quantidade": {"$gt":1}}},
        {"$group":{"_id":"$produtos.descricao"}},
    ])
        WriteAJson(r4, "Venda Multipla")