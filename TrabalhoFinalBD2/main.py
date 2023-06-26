# Felipe Henrique Conrado - 155
# Frederico Flauzino Wlassow - 153

from database import Database
from player_database import PlayerDatabase
from cli import PlayerCLI

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.235.14.178:7687", "neo4j", "utilization-hierarchies-itineraries")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
player_db = PlayerDatabase(db)

player_db.create_basketball_player("Stephen Curry", "30", "35")
player_db.create_basketball_player("Klay Thompson", "11", "33")
player_db.create_basketball_player("Kevin Durant", "35", "34")
player_db.create_basketball_player("Devin Booker", "1", "26")
player_db.create_basketball_player("Lebron James", "6", "38")
player_db.create_basketball_player("Anthony Davis", "2", "30")
player_db.create_basketball_player("Jimmy Butler", "22", "33")
player_db.create_basketball_player("Bam Adebayo", "13", "25")
player_db.create_basketball_player("Giannis Antetokounmpo", "34", "28")
player_db.create_basketball_player("Jrue Holiday", "32", "32")
player_db.create_basketball_player("Joel Embiid", "21", "29")
player_db.create_basketball_player("James Harden", "1", "33")
player_db.create_basketball_player("Luka Doncic", "77", "24")
player_db.create_basketball_player("Kyrie Irving", "2", "31")
player_db.create_basketball_player("Nikola Jokic", "15", "28")
player_db.create_basketball_player("Jamal Murray", "27", "26")

player_db.create_basketball_team("Golden State Warriors", "San Francisco", "Chase Center")
player_db.create_basketball_team("Phoenix Suns", "Phoenix", "Footprint Center")
player_db.create_basketball_team("Los Angeles Lakers", "Los Angeles", "Crypto.com Arena")
player_db.create_basketball_team("Miami Heat", "Miami", "Kaseya Center")
player_db.create_basketball_team("Milwaukee Bucks", "Milwaukee", "Fiserv Forum")
player_db.create_basketball_team("Philadelphia 76ers", "Philadelphia", "Wells Fargo Center")
player_db.create_basketball_team("Dallas Mavericks", "Dallas", "American Airlines Center")
player_db.create_basketball_team("Denver Nuggets", "Denver", "Ball Arena")

player_db.create_Joga_no("Stephen Curry", "Golden State Warriors")
player_db.create_Joga_no("Klay Thompson", "Golden State Warriors")
player_db.create_Joga_no("Kevin Durant", "Phoenix Suns")
player_db.create_Joga_no("Devin Booker", "Phoenix Suns")
player_db.create_Joga_no("Lebron James", "Los Angeles Lakers")
player_db.create_Joga_no("Anthony Davis", "Los Angeles Lakers")
player_db.create_Joga_no("Jimmy Butler", "Miami Heat")
player_db.create_Joga_no("Bam Adebayo", "Miami Heat")
player_db.create_Joga_no("Giannis Antetokounmpo", "Milwaukee Bucks")
player_db.create_Joga_no("Jrue Holiday", "Milwaukee Bucks")
player_db.create_Joga_no("Joel Embiid", "Philadelphia 76ers")
player_db.create_Joga_no("James Harden", "Philadelphia 76ers")
player_db.create_Joga_no("Luka Doncic", "Dallas Mavericks")
player_db.create_Joga_no("Kyrie Irving", "Dallas Mavericks")
player_db.create_Joga_no("Nikola Jokic", "Denver Nuggets")
player_db.create_Joga_no("Jamal Murray", "Denver Nuggets")

player_db.create_Ja_jogou_com("Lebron James", "Kyrie Irving")
player_db.create_Ja_jogou_com("Stephen Curry", "Kevin Durant")
player_db.create_Ja_jogou_com("Kyrie Irving", "Kevin Durant")
player_db.create_Ja_jogou_com("James Harden", "Kevin Durant")
player_db.create_Ja_jogou_com("Jrue Holiday", "Anthony Davis")
player_db.create_Ja_jogou_com("Jimmy Butler", "Joel Embiid")

playerCLI = PlayerCLI(player_db)
playerCLI.run()

# Fechando a conexão com o bd
db.close()
