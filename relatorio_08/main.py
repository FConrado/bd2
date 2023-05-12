from database import Database
from school_database import SchoolDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.239.245.255:7687", "neo4j", "threads-volumes-pronouns")
db.drop_all()

school_db = SchoolDatabase(db)

# Criando alguns players
school_db.create_player("Ana")
school_db.create_player("Carlos")
school_db.create_player("Beatriz")

# Criando algumas matches e suas relações com os professores
school_db.create_match("Ana, Pedro", "Ana")
school_db.create_match("Ana, Beatriz", "Beatriz")
school_db.create_match("Beatriz, Pedro", "Beatriz")

# Atualizando o nome de um professor
school_db.update_player("Carlos", "Pedro")

school_db.insert_player_match("Ana", "Ana, Pedro")
school_db.insert_player_match("Ana", "Ana, Beatriz")
school_db.insert_player_match("Pedro", "Beatriz, Pedro")
school_db.insert_player_match("Pedro", "Ana, Pedro")
school_db.insert_player_match("Beatriz", "Ana, Beatriz")
school_db.insert_player_match("Beatriz", "Beatriz, Pedro")

# Deletando um player e uma match
#school_db.delete_player("Beatriz")
#school_db.delete_match("História")

# Imprimindo todas as informações do banco de dados
print("players:")
print(school_db.get_players())
print("matches:")
print(school_db.get_matches())

# Fechando a conexão com o banco de dados
db.close()