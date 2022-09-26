from db.AulaDB import Crud
from Aula import Aula
from Aula import Professor
from Aula import Aluno

aulas = Crud()

repetirLoop1 = True
while(repetirLoop1 == True):

    print("Qual método deseja realizar?")
    print("1 - Criar uma aula")
    print("2 - Editar uma aula")
    print("3 - Apagar uma aula")
    print("4 - Sair do menu")
    opcao1 = input()

    if(opcao1 == '1'):
        print("Qual o assunto da aula?")
        assunto = input()
        aula = Aula(assunto)
        print("Qual o nome do professor?")
        nomeProf = input()
        print("Qual a especialidade do professor?")
        espProf = input()
        professor = Professor(nomeProf,espProf)
        aula.professor = professor
        print("Informe os dados dos alunos presentes na aula:")
        repetirLoop2 = True
        aula.alunos.clear()

        while(repetirLoop2 == True):

            print("Qual o nome do aluno?")
            nomeAluno = input()
            print("Qual a matricula do aluno?")
            matAluno = input()
            print("Qual o curso do aluno?")
            cursoAluno = input()
            print("Qual o período do aluno?")
            periodoAluno = input()
            aluno = Aluno(nomeAluno, matAluno, cursoAluno, periodoAluno)
            aula.alunos.append(aluno)
            print("Deseja adicionar mais um aluno a lista?")
            print("1 - sim")
            print("2 - não")
            opcao2 = input()
            if(opcao2 == '2'):
                repetirLoop2 = False
                aulas.create_aula(aula.assunto,aula.professor,aula.alunos)
                print("Aula criada")
                print("O que deseja fazer agora?")
                print("1 - Voltar ao menu")
                print("2 - Sair do menu")
                opcao10 = input()
                if(opcao10 == '2'):
                    repetirLoop1 = False


    elif(opcao1 == '2'):
        repetirLoop3 = True
        while(repetirLoop3 == True):
            print("Qual o ID da aula que gostaria de editar?")
            id = input()
            print("O que gostaria de editar?")
            print("1 - O assunto da aula")
            print("2 - O professor da aula")
            print("3 - Os alunos da aula")
            opcao3 = input()
            if(opcao3 == '1'):
                print("Informe o novo assunto:")
                upAssunto = input()
                aulas.update_assunto(id,upAssunto)
                print("Assunto da aula atualizado!")
                print("O que deseja fazer agora?")
                print("1 - Editar outra aula")
                print("2 - Voltar ao menu")
                print("3 - Sair do menu")
                opcao4 = input()
                if(opcao4 == '2'):
                    repetirLoop3 = False
                elif(opcao4 == '3'):
                    repetirLoop3 = False
                    repetirLoop1 = False

            elif(opcao3 == '2'):
                print("Informe as informações do novo professor:")
                print("Qual o nome do professor?")
                nomeProf = input()
                print("Qual a especialidade do professor?")
                espProf = input()
                professor = Professor(nomeProf, espProf)
                aulas.update_professor(id,professor)
                print("Professor da aula atualizado!")
                print("O que deseja fazer agora?")
                print("1 - Editar outra aula")
                print("2 - Voltar ao menu")
                print("3 - Sair do menu")
                opcao5 = input()
                if (opcao5 == '2'):
                    repetirLoop3 = False
                elif (opcao5 == '3'):
                    repetirLoop3 = False
                    repetirLoop1 = False

            elif(opcao3 == '3'):
                print("O que deseja fazer?")
                print("1 - Alterar toda a lista de alunos da aula")
                print("2 - Adicionar um novo aluno a aula")
                print("3 - Remover um aluno da aula")
                opcao5 = input()
                if(opcao5 == '1'):
                    print("Informe os dados dos alunos presentes na aula:")
                    repetirLoop4 = True
                    newAlunos: list[Aluno] = []
                    while (repetirLoop4 == True):
                        print("Qual o nome do aluno?")
                        nomeAluno = input()
                        print("Qual a matricula do aluno?")
                        matAluno = input()
                        print("Qual o curso do aluno?")
                        cursoAluno = input()
                        print("Qual o período do aluno?")
                        periodoAluno = input()
                        aluno = Aluno(nomeAluno, matAluno, cursoAluno, periodoAluno)
                        newAlunos.append(aluno)
                        print("Deseja adicionar mais um aluno a lista?")
                        print("1 - sim")
                        print("2 - não")
                        opcao2 = input()
                        if (opcao2 == '2'):
                            repetirLoop4 = False
                            aulas.update_allAlunos(id,newAlunos)
                            print("Alunos da aula atualizados!")
                            print("O que deseja fazer agora?")
                            print("1 - Editar outra aula")
                            print("2 - Voltar ao menu")
                            print("3 - Sair do menu")
                            opcao6 = input()
                            if (opcao6 == '2'):
                                repetirLoop3 = False
                            elif (opcao6 == '3'):
                                repetirLoop3 = False
                                repetirLoop1 = False


                elif(opcao5 == '2'):
                    print("Qual o nome do aluno?")
                    nomeAluno = input()
                    print("Qual a matricula do aluno?")
                    matAluno = input()
                    print("Qual o curso do aluno?")
                    cursoAluno = input()
                    print("Qual o período do aluno?")
                    periodoAluno = input()
                    aluno = Aluno(nomeAluno, matAluno, cursoAluno, periodoAluno)
                    aulas.update_aluno(id,aluno)
                    print("Aluno adicionado a lista!")
                    print("O que deseja fazer agora?")
                    print("1 - Editar outra aula")
                    print("2 - Voltar ao menu")
                    print("3 - Sair do menu")
                    opcao7 = input()
                    if (opcao7 == '2'):
                        repetirLoop3 = False
                    elif (opcao7 == '3'):
                        repetirLoop3 = False
                        repetirLoop1 = False

                elif(opcao5 == '3'):
                    print("Qual a matricula do aluno que deseja remover da aula?")
                    matAluno = input()
                    aulas.delete_aluno(id,matAluno)
                    print("Aluno removido da lista!")
                    print("O que deseja fazer agora?")
                    print("1 - Editar outra aula")
                    print("2 - Voltar ao menu")
                    print("3 - Sair do menu")
                    opcao8 = input()
                    if (opcao8 == '2'):
                        repetirLoop3 = False
                    elif (opcao8 == '3'):
                        repetirLoop3 = False
                        repetirLoop1 = False

    elif(opcao1 == '3'):
        repetirLoop4 = True
        while (repetirLoop4 == True):
            print("Qual o ID da aula que gostaria de remover?")
            id = input()
            aulas.delete_aula(id)
            print("Aula apagada!")
            print("O que deseja fazer agora?")
            print("1 - Apagar outra aula")
            print("2 - Voltar ao menu")
            print("3 - Sair do menu")
            opcao9 = input()
            if (opcao9 == '2'):
                repetirLoop4 = False
            elif (opcao9 == '3'):
                repetirLoop4 = False
                repetirLoop1 = False

    elif(opcao1 == '4'):
        repetirLoop1 = False