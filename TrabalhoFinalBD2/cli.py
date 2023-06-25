class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, number, function):
        self.commands[number] = function
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Insira um comando: ").lower()
            if (command == "sair" or "9"):
                print("Adeus!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido, tente novamente.")

class PlayerCLI(SimpleCLI):
    def __init__(self, player_model):
        super().__init__()
        self.player_model = player_model
        self.add_command("adicionar jogador", "1", self.create_basketball_player)
        self.add_command("checar jogador", "2", self.read_player)
        self.add_command("atualizar jogador", "3", self.update_player)
        self.add_command("deletar Jogador", "4", self.delete_player)
        self.add_command("adicionar time", "5", self.create_basketball_team)
        self.add_command("checar time", "6", self.read_team)
        self.add_command("atualizar time", "7", self.update_team)
        self.add_command("deletar time", "8", self.delete_team)

    def create_basketball_player(self):
        name = input("Insira o nome do jogador: ")
        number = int(input("Insira o número do jogador: "))
        age = int(input("Insira a idade do jogador: "))

        self.player_model.create_basketball_player(name, number, age)

        time = input(name + " joga para que time?").title()
        print(time)
        self.player_model.create_Joga_no(name, time)
        x = input(name + " já jogou com um jogador profissional? 1-Sim  2-Não" )
        while(x.lower() == "sim" or x == "1"):
            name2 = input("Com quem " + name + " jogou? ").title()
            print(name2)
            self.player_model.create_Ja_jogou_com(name, name2)
            x = input("Deseja adicionar mais um jogador com quem " + name + " jogou? 1-Sim 2-Não" )
     

    def create_basketball_team(self):
        name = input("Insira o nome do time: ")
        city = input("Insira a cidade: ")
        arena = input("Insira a arena: ")

        self.player_model.create_basketball_team(name, city, arena)

    def read_player(self):
        id = int(input("Insira a id: "))
        player = self.player_model.read_player_by_id(id)
        if player:
            _properties = player[0]._properties
            name = _properties.get('name')
            number = _properties.get('number')
            age = _properties.get('age')
            if name:
                print(f"Nome: {name}")
            if number:
                print(f"Número: {number}")
            if age:
                print(f"Idade: {age} "+" anos")
        else:
            print("Player não encontrado")

    def read_team(self):
        id = int(input("Insira a id: "))
        team = self.player_model.read_team_by_id(id)
        if team:
            _properties = team[0]._properties
            name = _properties.get('name')
            cidade = _properties.get('cidade')
            arena = _properties.get('arena')
            if name:
                print(f"Name: {name}")
            if cidade:
                print(f"Cidade: {cidade}")
            if arena:
                print(f"Arena: {arena}")
        else:
            print("Time não encontrado")
    
    def update_player(self):
        name = input("Qual jogador deseja atualizar?: ")
        name2 = input("Insira um novo nome: ")
        number = input("Insira o novo número: ")
        age = input("Insira a nova idade: ")
        self.player_model.update_player(name, name2, number, age)

    def update_team(self):
        name = input("Qual time deseja atualizar? ")
        name2 = input("Insira o novo nome do time: ")
        cidade = input("Insira a nova cidade: ")
        arena = input("Insira o novo nome da arena: ")
        self.player_model.update_team(name, name2, cidade, arena)

    def delete_player(self):
        name = input("Qual jogador deseja excluir? ")
        self.player_model.delete_player(name)
        print(name + " foi excluído!")

    def delete_team(self):
        name = input("Qual time deseja excluir? ")
        self.player_model.delete_player(name)
        print(name + " foi excluído!")

    def run(self):
        print("Bem-vindo ao projeto final de Laboratório de Banco de Dados 2!")
        print("----------------------")
        print("Comandos Disponíveis: 1) Adicionar jogador  2) Checar jogador  3) Atualizar jogador  4) Deletar Jogador")
        print("5) Adicionar time     6) Checar time        7) Atualizar time  8) Deletar time       9) Sair")
        super().run()