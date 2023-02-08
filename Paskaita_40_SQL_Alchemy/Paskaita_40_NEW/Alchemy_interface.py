from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Alchemy_class import Asmuo, Bankas, Saskaita

engine = create_engine('sqlite:///finansai.db')
Session = sessionmaker(bind=engine)
session = Session()

while True:
    selektas = int(input("Pasirinkite: \n1 - Ivesti naujus duomenis: \n2 - Perziureti saskaitas: \n3 - Prideti pinigu: \n4 - nuimti pinigu: \n5 - Iseiti: "))
    if selektas == 1:
        selectas1 = int(input("Pasirinkite: \n1 - Ivesti asmeni: \n2 - Ivesti banka: "))
        if selectas1 == 1:
            saskaita = Saskaita(vardas="Vaikas", pavarde="Vaikaitis")
            vaikas2 = Vaikas(vardas="Vaikas 2", pavarde="Vaikaitis 2")
            tevas = Tevas(vardas="Tevas", pavarde="Vaikaitis")
            tevas.vaikai.append(vaikas)
            tevas.vaikai.append(vaikas2)
            session.add(tevas)
            session.commit()