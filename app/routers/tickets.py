from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from ..orm.models import Ticket, Comprador

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/check-ticket/ticket={ticket}&ticket_pass={ticket_pass}")
def check_ticket(ticket: int, ticket_pass: str, db: Session = Depends(get_db)):
    db_ticket = db.query(Ticket).filter(Ticket.id_ticket == ticket).first()
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    if db_ticket.ticket_pass != ticket_pass:
        raise HTTPException(status_code=400, detail="Incorrect password")
    
    if db_ticket.registrado:
        raise HTTPException(status_code=400, detail="Ticket already registered")
    
    db_ticket.registrado = True
    db.commit()
    db.refresh(db_ticket)
    
    return {"message": "Contraseña correcta"}

@router.post("/register-comprador/name={name}&last_name={last_name}&email={email}&phone={phone}&id_ticket={id_ticket}")
def register_comprador(name: str, last_name: str, email: str, phone: int, id_ticket: int, db: Session = Depends(get_db)):
    db_comprador = db.query(Comprador).filter(Comprador.phone == phone).first()    
    if db_comprador:
        id_comprador = db_comprador.id_comprador
    else:
        new_comprador = Comprador(name=name, last_name=last_name, email=email, phone=phone)
        db.add(new_comprador)
        db.commit()
        db.refresh(new_comprador)
        id_comprador = new_comprador.id_comprador    
    db_ticket = db.query(Ticket).filter(Ticket.id_ticket == id_ticket).first()
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    db_ticket.id_comprador = id_comprador
    db.commit()
    db.refresh(db_ticket)
    
    return {"message": "Comprador registrado"}
