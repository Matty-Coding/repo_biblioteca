
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Tabella libri
class Libro(db.Model):
    __tablename__ = "libri"
    id = Column(Integer, primary_key=True, autoincrement=True)
    autore = Column(String(255), nullable=False)
    titolo = Column(String(255), nullable=False, unique=True)
    genere = Column(String(255), nullable=False)
    totale_libri = Column(Integer, nullable=False) 

    # Relazione tra tabelle prestiti-libri
    prestiti = relationship("Prestito", back_populates="libro")

    def __init__(self, autore, titolo, genere, totale_libri):
        self.autore = autore
        self.titolo = titolo
        self.genere = genere
        self.totale_libri = totale_libri

# =============================================
# =============================================
# =============================================


# Tabella utenti
class Utente(db.Model):
    __tablename__ = "utenti"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    cognome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    telefono = Column(String(255), nullable=False, unique=True)

    # Relazione tra tabelle prestiti-utenti
    prestiti = relationship("Prestito", back_populates="utente")

    def __init__(self, nome, cognome, email, telefono):
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.telefono = telefono


# ==========================================
# ==========================================
# ==========================================
    

# Tabella prestiti
class Prestito(db.Model):
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

    def __init__(self, id_libro, id_utente, data_inizio, data_fine=None):
        self.id_libro = id_libro
        self.id_utente = id_utente
        self.data_inizio = data_inizio
        self.data_fine = data_fine
