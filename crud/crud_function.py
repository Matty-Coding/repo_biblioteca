
from models import Libro, Utente, Prestito, db
from datetime import datetime
from werkzeug.security import generate_password_hash

# Operazioni CRUD sui libri
class CRUD_Libro:
    
    # CREATE
    
    @staticmethod
    def create(autore, titolo, genere, totale_libri) -> dict:
        libro = Libro(autore, titolo, genere, totale_libri)
        
        try:
            db.session.add(libro)
            db.session.commit()
            
            return {"operazione":True, "risultato":libro.to_dict()}
        
        except Exception as e:
            db.session.rollback()
            
            return {"operazione":False, "risultato":str(e)}
        
    # READ 
    
    @staticmethod
    def read_all() -> list:
        return db.session.query(Libro).all()
    
    @staticmethod
    def read_id(id_libro:int) -> Libro | None:
        return db.session.get(Libro, id_libro)
    
    @staticmethod
    def read_title(titolo:str) -> Libro | None:
        return db.session.query(Libro).filter_by(titolo=titolo).first()
    
    @staticmethod
    def read_author(autore:str) -> list:
        return db.session.query(Libro).filter_by(autore=autore).all()
    
    @staticmethod
    def read_genre(genere:str) -> list:
        return db.session.query(Libro).filter_by(genere=genere).all()
    
    
    # UPDATE 
    
    @staticmethod
    def update(id_libro:int, autore=None, titolo=None, genere=None, totale_libri=None) -> dict:
        try:
            libro = db.session.get(Libro, id_libro)
            
            if not libro:
                return {"operazione":False, "risultato":"Libro non trovato, impossibile completare l'operazione."}
            
            if autore is not None:
                libro.autore = autore
                
            if titolo is not None:
                libro.titolo = titolo
                
            if genere is not None:
                libro.genere = genere
                
            if totale_libri is not None:
                libro.totale_libri = totale_libri
            
            db.session.commit()
            
            return {"operazione":True, "risultato":libro.to_dict()}
        
        except Exception as e:
            db.session.rollback()
            
            return {"operazione":False, "risultato":str(e)}
        
        
    # DELETE
    @staticmethod
    def delete(id_libro:int) -> dict:
        try:
            libro = db.session.get(Libro, id_libro)
            
            if not libro:
                return {"operazione":False, "risultato":"Libro non trovato, impossibile completare l'operazione."}
            
            db.session.delete(libro)
            db.session.commit()
            
            return {"operazione":True, "risultato":libro.to_dict()}
        
        except Exception as e:
            db.session.rollback()
            
            return {"operazione":False, "risultato":str(e)}
        
        
# =======================================
# =======================================
# =======================================

# CORREGGI CREAZIONE SE ARRIVANO INPUT NON VALIDI

# Operazioni CRUD sugli utenti
class CRUD_Utente:
    
    # CREATE 
    
    @staticmethod
    def create(nome:str, cognome:str, email:str, telefono:str, password:str) -> dict:
        # if not all([nome, cognome, email, telefono, password]):
        #     return {"operazione":False, "risultato":"Campi mancanti o non validi, impossibile creare nuovo utente."}
        utente = Utente(nome, cognome, email, telefono, password)
        try:
            # utente = Utente(nome, cognome, email, telefono, password)
            db.session.add(utente)
            db.session.commit()
            
            return {"operazione":True, "risultato":utente.to_dict()}
        
        except Exception as e:
            db.session.rollback()
            
            return {"operazione":False, "risultato":str(e)}
        
    # READ
    
    @staticmethod
    def read_all() -> list:
        return db.session.query(Utente).all()
    
    @staticmethod
    def read_id(id_utente:int) -> Utente | None:
        return db.session.get(Utente, id_utente)
    
    @staticmethod
    def read_name(nome:str) -> list:
        return db.session.query(Utente).filter_by(nome=nome).all()
    
    @staticmethod
    def read_surname(cognome:str) -> list:
        return db.session.query(Utente).filter_by(cognome=cognome).all()
    
    @staticmethod
    def read_email(email:str) -> Utente | None:
        return db.session.query(Utente).filter_by(email=email).first()
    
    @staticmethod
    def read_phone(telefono:str) -> Utente | None:
        return db.session.query(Utente).filter_by(telefono=telefono).first()
    
    # UPDATE
    
    @staticmethod
    def update(id_utente:int, nome=None, cognome=None, email=None, telefono=None, password=None) -> dict:
        try:
            utente = db.session.get(Utente, id_utente)
            
            if not utente:
                return {"operazione":False, "risultato":"Utente non trovato, impossibile completare l'operazione."}
            
            if nome is not None:
                utente.nome = nome
    
            if cognome is not None:
                utente.cognome = cognome
    
            if email is not None:
                utente.email = email
    
            if telefono is not None:
                utente.telefono = telefono
    
            if password is not None:
                utente.password_hash = generate_password_hash(password)
                
            db.session.commit()
            
            return {"operazione":True, "risultato":utente.to_dict()}
        
        except Exception as e:
            db.session.rollback()
            
            return {"operazione":False, "risultato":str(e)}
    
    # DELETE
    
    @staticmethod
    def delete(id_utente:int) -> dict:
        try:
            utente = db.session.get(Utente, id_utente)
            if not utente:
                return {"operazione":False, "risultato":"Utente non trovato, impossibile completare l'operazione."}
    
            db.session.delete(utente)
            db.session.commit()

            return {"operazione":True, "risultato":utente.to_dict()}
        
        except Exception as e:
            db.session.rollback()
            
            return {"operazione":False, "risultato":str(e)}
        


# =======================================
# =======================================
# =======================================


# Operazioni CRUD sui prestiti
class CRUD_Prestito:
    
    # CREATE
    
    @staticmethod
    def create(id_libro:int, id_utente:int, data_inizio:str, data_fine:str) -> dict:
        data_inizio = datetime.strptime(data_inizio, "%d/%m/%y").date()
        data_fine = datetime.strptime(data_fine, "%d/%m/%y").date()
        
        prestito = Prestito(id_libro, id_utente, data_inizio, data_fine)
        try:
            db.session.add(prestito)
            db.session.commit()
            
            return {"operazione":True, "risultato":prestito.to_dict()}

        except Exception as e:
            db.session.rollback()
            
            return {"operazione":False, "risultato":str(e)}
        
    # READ 
    
    @staticmethod
    def read_all() -> list:
        return db.session.query(Prestito).all()  
    
    @staticmethod
    def read_book_id(id_libro:int) -> list:
        return db.session.query(Prestito).filter_by(id_libro=id_libro).all()
    
    @staticmethod
    def read_user_id(id_utente:int) -> Prestito | None:
        return db.session.query(Prestito).filter_by(id_utente=id_utente).first()
    
    # UPDATE
    
    @staticmethod
    def update(id_prestito:int, data_fine=None) -> dict:
        try:
            prestito = db.session.get(Prestito, id_prestito)
            if not prestito:
                return {"operazione":False, "risultato":"Prestito non trovato, impossibile completare l'operazione."}
            
            if data_fine is not None:
                data_fine = datetime.strptime(data_fine, "%d/%m/%y").date()
                prestito.data_fine = data_fine
                
            db.session.commit()
    
            return {"operazione":True, "risultato":prestito.to_dict()}

        except Exception as e:
            db.session.rollback()
        
            return {"operazione":False, "risultato":str(e)}
        
    # DELETE
    
    @staticmethod
    def delete(id_prestito:int) -> dict:
        try:
            prestito = db.session.get(Prestito, id_prestito)
            if not prestito:
                return {"operazione":False, "risultato":"Prestito non trovato, impossibile completare l'operazione."}
            
            db.session.delete(prestito)
            db.session.commit()
            
            return {"operazione":True, "risultato":prestito.to_dict()}
        
        except Exception as e:
            db.session.rollback()
            
            return {"operazione":False, "risultato":str(e)}
        
