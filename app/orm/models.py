from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Vendedor(Base):
    __tablename__ = "vendedores"

    id_vendedor = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    last_name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)
    phone = Column(Integer)


class Comprador(Base):
    __tablename__ = "compradores"

    id_comprador = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    last_name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)
    phone = Column(Integer)


class Ticket(Base):
    __tablename__ = "tickets"

    id_ticket = Column(Integer, primary_key=True, index=True)
    ticket_pass = Column(String(8))
    id_vendedor = Column(Integer, ForeignKey("vendedores.id_vendedor"))
    id_comprador = Column(Integer, ForeignKey("compradores.id_comprador"), nullable=True)
    registrado = Column(Boolean, default=False)
