from database import Database
from MotoristaDAO import MotoristaDAO
from MotoristaCLI import MotoristaCLI

db = Database(database="Avaliacao", collection="Motoristas")
motoristaDAO = MotoristaDAO(database=db)


motoristaCLI = MotoristaCLI(motoristaDAO)
motoristaCLI.run()