class PlayerDatabase:
    def __init__(self, database):
        self.db = database

    # CREATE
    def create_basketball_player(self, name, number, age):
        query = "CREATE (:Player {name: $name, number: $number, age: $age})"
        parameters = {"name": name, "number": number, "age": age}
        self.db.execute_query(query, parameters)

    def create_basketball_team(self, name, cidade, arena):
        query = "CREATE (:Team {name: $name, cidade: $cidade, arena: $arena})"
        parameters = {"name": name, "cidade": cidade, "arena": arena}
        self.db.execute_query(query, parameters)

    def create_Joga_no(self, nome_player, nome_team):
        query = "MATCH(p:Player{name: $nome_player}), (t:Team{name: $nome_team}) CREATE (p)-[:Joga_no]->(t)"
        parameters = {"nome_player": nome_player, "nome_team": nome_team}
        self.db.execute_query(query, parameters)

    def create_Ja_jogou_com(self, nome_player, nome_player2):
        query = "MATCH(p:Player{name: $nome_player}), (q:Player{name: $nome_player2}) CREATE (p)-[:Ja_Jogou_Com]->(q)"
        parameters = {"nome_player": nome_player, "nome_player2": nome_player2}
        self.db.execute_query(query, parameters)

    # READ
    def read_player_by_id(self, id):
        query = "MATCH (p:Player) where id(p) = $ID RETURN p AS player_name"
        parameters = {"ID": id}
        results = self.db.execute_query(query, parameters)
        return [result["player_name"] for result in results]
    
    def read_team_by_id(self, id):
        query = "MATCH (t:Team) where id(t) = $ID RETURN t AS team_name"
        parameters = {"ID": id}
        results = self.db.execute_query(query, parameters)
        return [result["team_name"] for result in results]
    
    # UPDATE

    def update_player(self, name, newName, newNumber, newAge):
        query = "MATCH (p:Player {name: $name}) SET p.name = $newName, p.number = $newNumber, p.age = $newAge"
        parameters = {"name": name, "newName": newName, "newNumber": newNumber, "newAge": newAge}
        self.db.execute_query(query, parameters)

    def update_team(self, name, newName, newcidade, newArena):
        query = "MATCH (t:Team {name: $name}) SET t.name = $newName, t.arena = $newArena, t.city = $newcidade"
        parameters = {"name": name, "newName": newName, "newArena": newArena, "newcidade": newcidade}
        self.db.execute_query(query, parameters)

    #DELETE

    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_team(self, name):
        query = "MATCH (t:Team {name: $name}) DETACH DELETE t"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

