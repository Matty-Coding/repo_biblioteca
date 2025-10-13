
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash 
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()


# Tabella libri
class Libro(db.Model):
    def __init__(self, autore, titolo, genere, totale_libri):
        self.autore = autore
        self.titolo = titolo
        self.genere = genere
        self.totale_libri = totale_libri

    __tablename__ = "libri"
    id = Column(Integer, primary_key=True, autoincrement=True)
    autore = Column(String(255), nullable=False)
    titolo = Column(String(255), nullable=False, unique=True)
    genere = Column(String(255), nullable=False)
    totale_libri = Column(Integer, nullable=False) 

    # Relazione tra tabelle prestiti-libri
    prestiti = relationship("Prestito", back_populates="libro")
    
    def to_dict(self):
        return {
            "id" : self.id,
            "autore" : self.autore,
            "titolo" : self.titolo,
            "genere" : self.genere,
            "totale_libri" : self.totale_libri
        }
        
    def __str__(self):
        return str(self.to_dict())

# =============================================
# =============================================
# =============================================


# Tabella utenti
# UserMixin aggiunge automaticamente:
# - is_authenticated
# - is_active
# - is_anonymous
# - get_id()
# questi metodi vengono usati da flask_login per capire chi è loggato
class Utente(db.Model, UserMixin):
    def __init__(self, nome, cognome, email, telefono, password):
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.telefono = telefono
        self.password_hash = generate_password_hash(password)
        
    __tablename__ = "utenti"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    cognome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    telefono = Column(String(10), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    
    # Relazione tra tabelle prestiti-utenti
    prestiti = relationship("Prestito", back_populates="utente")

    def to_dict(self):
        return {
            "id" : self.id,
            "nome" : self.nome,
            "cognome" : self.cognome,
            "email" : self.email,
            "telefono" : self.telefono,
        }

    def verifica_password(self, password):
        return check_password_hash(self.password_hash, password)
        
    def __str__(self):
        return str(self.to_dict())
    
    
    
# ==========================================
# ==========================================
# ==========================================
    

# Tabella prestiti
class Prestito(db.Model):
    def __init__(self, id_libro, id_utente, data_inizio, data_fine=None):
        self.id_libro = id_libro
        self.id_utente = id_utente
        self.data_inizio = data_inizio
        self.data_fine = data_fine
    
    __tablename__ = "prestiti"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_libro = Column(Integer, ForeignKey("libri.id"), nullable=False)
    id_utente = Column(Integer, ForeignKey("utenti.id"), nullable=False)
    data_inizio = Column(Date, nullable=False)
    data_fine = Column(Date, nullable=True)

    # Relazione tra tabelle libri-prestiti
    libro = relationship("Libro", back_populates="prestiti")
    
    # Relazione tra tabelle utenti-prestiti
    utente = relationship("Utente", back_populates="prestiti")

    def to_dict(self):
        return {
            "id" : self.id,
            "id_libro" : self.id_libro,
            "id_utente" : self.id_utente,
            "data_inizio" : datetime.strftime(self.data_inizio, "%d/%m/%y") if self.data_inizio else None,
            "data_fine" : datetime.strftime(self.data_fine, "%d/%m/%y") if self.data_fine else None
        }
        
    def __str__(self):
        return str(self.to_dict())
    
    