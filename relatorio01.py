class Professor:

    def __init__(self, nome):
        self.nome = nome

    def cumprimentar(self, assunto):
        print(f'O professor ' + self.nome + ' esta ministrando uma aula sobre ' + assunto)

class Aluno:
    
    def __init__(self, nome):
        self.nome = nome

    def presenca(self, assunto):
        print(f'O aluno ' + self.nome + ' esta presente')

class Aula:
    def __init__(self, professor, assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []

    def adicionar_aluno(self, nome):
        self.alunos.append(nome)

    def listar_presenca(self):
        print(f'Presenca na aula sobre ' + self.assunto + ", ministrada pelo professor " + self.professor.nome + ":")
        for x in self.alunos:
            print(x.nome)

class Main:
    professor = Professor("Lucas")
    aluno1 = Aluno("Maria")
    aluno2 = Aluno("Pedro")
    aula = Aula(professor, "Programação Orientada a Objetos")
    aula.adicionar_aluno(aluno1)
    aula.adicionar_aluno(aluno2)
    print(aula.listar_presenca())
