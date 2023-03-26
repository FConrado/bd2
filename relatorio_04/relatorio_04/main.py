from ProductAnalyzer import ProductAnalyzer
from database import Database

db = Database(database="mercado", collection="compras")
db.resetDatabase()

productAnalyzer = ProductAnalyzer("mercado", "compras")

productAnalyzer.venda()
productAnalyzer.top_sale()
productAnalyzer.top_cliente()
productAnalyzer.maisDeUmaVenda()