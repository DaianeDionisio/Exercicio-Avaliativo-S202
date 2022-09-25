class Pessoa(object):
    def __init__(self,nome):
        self.nome = nome

class Aluno(Pessoa):
    def __init__(self,nome,matricula,curso,periodo):
        super().__init__(nome)
        self.matricula = matricula
        self.curso = curso
        self.periodo = periodo

    def toString(self):
        print(' nome: '+ self.nome)
        print(' matricula: {0}'.format(self.matricula))
        print(' curso: ' + self.curso)
        print(' periodo: {0}\n'.format(self.periodo))

class Professor(Pessoa):
    def __init__(self,nome,especialidade):
        super().__init__(nome)
        self.especialidade = especialidade

    def toString(self):
        print(' Professor: '+ self.nome)

class Aula():
    def __init__(self,assunto):
        self.assunto = assunto
        self.professor: Professor = None
        self.alunos: list[Aluno] = []

    def getListaPresenca(self):
        print('Aula de '+ self.assunto)
        self.professor.toString()
        print('Alunos Presentes:')
        for i in self.alunos:
            i.toString()