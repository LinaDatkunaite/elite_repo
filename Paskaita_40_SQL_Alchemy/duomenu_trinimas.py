from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alchemy_paskaita import Projektas

engine = create_engine('sqlite:///projektai.db')
Session = sessionmaker(bind=engine)
session = Session()


# projektas1 = session.query(Projektas).filter_by(name="Naujas pr.").one()
# session.delete(projektas1)
# session.commit()


# Kitoks (dazniausiai daugelio) objekto trynimas
projektai = session.query(Projektas).all()
print(len(projektai))
projektai.remove(projektai[0])
session.commit()
session.close()



# projektas2 = session.query(Projektas).get(4)
# session.delete(projektas2)
# session.commit()

