
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alchemy_paskaita import Projektas

engine = create_engine('sqlite:///projektai.db')
Session = sessionmaker(bind=engine)
session = Session()


# projektas1 = session.query(Projektas).get(2)
# projektas1.price = 30000
# session.commit()
# session.close()


projektai = session.query(Projektas).all()
print(projektai)
for projektas in projektai:
    print(projektas.id, projektas.name, projektas.price)


