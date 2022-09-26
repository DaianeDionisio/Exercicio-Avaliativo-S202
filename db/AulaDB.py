from db.database import Database
from bson.objectid import ObjectId

class Crud:
    def __init__(self):
        self.db = Database(database="inatel",collection="Aulas")
        self.collection = self.db.collection

    #cria uma nova aula
    def create_aula(self, assunto: str, professor: object, alunos: list):
        res = self.collection.insert_one({

            "assunto": assunto,
            "professor": {
                "nome": getattr(professor,'nome'),
                "especialidade": getattr(professor,'especialidade')
            }
        })

        x = len(alunos)
        for i in range (x):
            self.collection.update_one(
                {"_id": res.inserted_id},{"$push": {
                    "alunos": {
                        "nome": getattr(alunos[i],'nome'),
                        "matricula": getattr(alunos[i],'matricula'),
                        "curso": getattr(alunos[i],'curso'),
                        "periodo": getattr(alunos[i],'periodo')
                    }
                }
            })
        return res.inserted_id

    #le todas as aulas do banco
    def read_aula(self):
        res = self.collection.find()
        return res

    #atualiza
    def update_assunto(self, id: str, assunto: str):
        res = self.collection.update_one({"_id": ObjectId(id)},{"$set": {"assunto": assunto}})
        return res.modified_count

    #atualiza
    def update_professor(self, id: str, professor: object):
        res = self.collection.update_one({"_id": ObjectId(id)},{"$set": {
            "professor": {
                "nome": getattr(professor,'nome'),
                "especialidade": getattr(professor,'especialidade')
            }
        }})
        return res.modified_count

    #apagar toda a lista de alunos e adiciona uma nova
    def update_allAlunos(self, id: str, alunos: list):
        self.collection.update_one({"_id": ObjectId(id)}, {"$set": {"alunos": []}})

        x = len(alunos)
        for i in range(x):
            res = self.collection.update_one(
                {"_id": ObjectId(id)}, {"$push": {
                    "alunos": {
                        "nome": getattr(alunos[i], 'nome'),
                        "matricula": getattr(alunos[i], 'matricula'),
                        "curso": getattr(alunos[i], 'curso'),
                        "periodo": getattr(alunos[i], 'periodo')
                    }
                }
            })
        return res.modified_count

    #adiciona 1 aluno a aula
    def update_aluno(self, id: str, aluno: object):

        res = self.collection.update_one(
            {"_id": ObjectId(id)}, {"$push": {
                "alunos": {
                    "nome": getattr(aluno, 'nome'),
                    "matricula": getattr(aluno, 'matricula'),
                    "curso": getattr(aluno, 'curso'),
                    "periodo": getattr(aluno, 'periodo')
                }
            }
        })
        return res.modified_count

    #apaga o aluno da lista de acordo com a matricula
    def delete_aluno(self, id: str, matAluno: str):
        res = self.collection.update_one(
            {"_id": ObjectId(id)}, {"$pull": {
                "alunos": {
                    "matricula": matAluno
                }
            }
            })
        return res.modified_count

    #apaga a aula
    def delete_aula(self, id: str):
        res = self.collection.delete_one({"_id": ObjectId(id)})
        return res.deleted_count

