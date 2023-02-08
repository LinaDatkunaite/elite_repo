from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///finansai.db')
Base = declarative_base()


class Asmuo(Base):
    __tablename__ = "asmuo"
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavardė", String)
    asmens_kodas = Column("asmens_kodas", String, unique=True)
    tel_nr = Column("tel_nr", String, unique=True)
    saskaitos = relationship("Saskaita", back_populates="asmuo")


class Bankas(Base):
    __tablename__ = "bankas"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column("pavadinimas", String)
    adresas = Column("adresas", String)
    banko_kodas = Column("banko_kodas", String, unique=True)
    swift = Column("swift", String, unique=True)
    saskaitos = relationship("Saskaitos", back_populates="bankas")


class Saskaita(Base):
    __tablename__ = "saskaita"
    id = Column(Integer, primary_key=True)
    sask_nr = Column("sask_nr", String)
    balansas = Column("balansas", Float)
    asmuo_id = Column(Integer, ForeignKey("asmuo.id"))
    asmuo = relationship("Asmuo", back_populates="saskaitos")
    bankas_id = Column(Integer, ForeignKey("bankas.id"))
    bankas = relationship("Bankas", back_populates="saskaitos")


Base.metadata.create_all(engine)



---------------------------------------------


class Asmuo(Base):
    __tablename__ = "asmuo"
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavardė", String)
    asmens_kodas = Column("Asmens kodas", Integer, unique=True)
    tel_numeris = Column("Telefono numerius", String)

class Bankas(Base):
    __tablename__ = "bankas"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column("Pavadinimas", String)
    adresas = Column("Adresas", String)
    banko_kodas = Column("Banko kodas", Integer)
    swift_kodas = Column("SWIFT kodas", String)

class Saskaita(Base):
    __tablename__ = "saskaita"
    id = Column(Integer, primary_key=True)
    numeris = Column("Sąskaitos numeris", Integer)
    balansas = Column("Pinigų balansas", Float)
    asmuo_id = Column(Integer, ForeignKey('asmuo.id'))
    asmuo = relationship("Asmuo")
    bankas_id = Column(Integer, ForeignKey('bankas.id'))
    bankas = relationship("Bankas")