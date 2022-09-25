from db.AulaDB import Crud
from Aula import Aula
from Aula import Professor
from Aula import Aluno

aulas = Crud()

repetirLoop1 = True
while(repetirLoop1 == True):

    print("Qual método deseja realizar?\n")
    print("1 - Criar uma aula\n")
    print("2 - Editar uma aula\n")
    print("3 - Apagar uma aula\n")
    print("4 - Sair do menu\n")
    opcao1 = input()

    if(opcao1 == '1'):
        print("Qual o assunto da aula?")
        assunto = input()
        aula = Aula(assunto)
        print("Qual o nome do professor?\n")
        nomeProf = input()
        print("Qual a especialidade do professor?\n")
        espProf = input()
        professor = Professor(nomeProf,espProf)
        aula.professor = professor
        print("Informe os dados dos alunos presentes na aula:\n")
        repetirLoop2 = True

        while(repetirLoop2 == True):

            print("Qual o nome do aluno?\n")
            nomeAluno = input()
            print("Qual a matricula do aluno?\n")
            matAluno = input()
            print("Qual o curso do aluno?\n")
            cursoAluno = input()
            print("Qual o período do aluno?\n")
            periodoAluno = input()
            aluno = Aluno(nomeAluno, matAluno, cursoAluno, periodoAluno)
            aula.alunos.append(aluno)
            print("Deseja adicionar mais um aluno a lista?\n")
            print("1 - sim\n")
            print("2 - não\n")
            opcao2 = input()
            if(opcao2 == '2'):
                repetirLoop2 = False
                aulas.create_aula(aula.assunto,aula.professor,aula.alunos)
                print("Aula criada")


    if(opcao1 == '4'):
        repetirLoop1 = False

















