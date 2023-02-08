from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alchemy_paskaita import Projektas

engine = create_engine('sqlite:///projektai.db')
Session = sessionmaker(bind=engine)
session = Session()
""":type: sqlalchemy.orm.Session"""

projektas1 = Projektas("Naujas pr.", 20000)
session.add(projektas1)
session.commit()

projektas2 = Projektas("2 projektas", 55000)
session.add(projektas2)
session.commit()

projektai = session.query(Projektas).all()

for projektas in projektai:
    print(projektas.name, projektas.price)