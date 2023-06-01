from database import Database
from query import Query
from teacher_crud import TeacherCRUD
from cli import TeacherCLI

db = Database("bolt://54.86.202.240:7687", "neo4j", "wills-remedies-admiralties")

query_db = Query(db)
teacher_db = TeacherCRUD(db)

#Q1
print(query_db.questaoA())
print(query_db.questaoB())
print(query_db.questaoC())
print(query_db.questaoD())

#Q2
print(query_db.questao2A())
print(query_db.questao2B())
print(query_db.questao2C())
print(query_db.questao2D())

#Q3
teacherCLI = TeacherCLI(teacher_db)
teacherCLI.run()

db.close()