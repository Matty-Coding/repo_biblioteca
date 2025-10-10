
from models import Libro, Utente, Prestito, db


# Operazioni CRUD sui libri
class CRUD_Libro:
    
    # CREATE
    
    @staticmethod
    def create(autore, titolo, genere, totale_libri):
        libro = Libro(autore, titolo, genere, totale_libri)
        
        try:
            db.session.add(libro)
            db.session.commit()
            
            return {"operazione":True, "risultato":libro}
        
        except Exception as e:
            db.session.rollback()
            
            return {"operazione":False, "risultato":str(e)}
        
    # READ 
    
    @staticmethod
    def read_all():
        return db.session.query(Libro).all()
    
    @staticmethod
    def read_id(id_libro):
        return db.session.get(Libro, id_libro)
    
    @staticmethod
    def read_title(titolo):
        return db.session.query(Libro).filter_by(titolo=titolo).first()
    
    @staticmethod
    def read_author(autore):
        return db.session.query(Libro).filter_by(autore=autore).all()
    
    @staticmethod
    def read_genre(genere):
        return db.session.query(Libro).filter_by(genere=genere).all()
    
    
    # UPDATE 
    
    @staticmethod
    def update(id_libro, autore=None, titolo=None, genere=None, totale_libri=None):
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
            
            return {"operazione":True, "risultato":libro}
        
        except Exception as e:
            db.session.rollback()
            
            return {"operazione":False, "risultato":str(e)}
        
        
    # DELETE
    @staticmethod
    def delete(id_libro):
        try:
            libro = db.session.get(Libro, id_libro)
            
            if not libro:
                return {"operazione":False, "risultato":"Libro non trovato, impossibile completare l'operazione."}
            
            db.session.delete(libro)
            db.session.commit()

            return {"operazione":True, "risultato":libro}
        
        except Exception as e:
            db.session.rollback()
            
            return {"operazione":False, "risultato":str(e)}
        
        
# =======================================
# =======================================
# =======================================


# Operazioni CRUD sugli utenti
class CRUD_Utente:
    
    # CREATE 
    
    @staticmethod
    def create(nome, cognome, email, telefono):
        utente = Utente(nome, cognome, email, telefono)
        try:
            db.session.add(utente)
            db.commit()
            
            return {"operazione":True, "risultato":utente}
        
        except Exception as e:
            db.session.rollback()
            
            return {"operazione":False, "risultato":str(e)}
        
    # READ
    
    @staticmethod
    def read_all():
        return db.session.query(Utente).all()
    
    @staticmethod
    def read_id(id_utente):
        return db.session.get(Utente, id_utente).first()
    
    @staticmethod
    def read_name(nome):
        return db.session.query(Utente).filter_by(nome=nome).all()
    
    @staticmethod
    def read_surname(cognome):
        return db.session.query(Utente).filter_by(cognome=cognome).all()
    
    @staticmethod
    def read_email(email):
        return db.session.query(Utente).filter_by(email=email).first()
    
    @staticmethod
    def read_phone(telefono):
        return db.session.query(Utente).filter_by(telefono=telefono).first()
    
    # UPDATE
    
    @staticmethod
    def update(id_utente, nome=None, cognome=None, email=None, telefono=None):
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
    
            db.session.commit()
            
            return {"operazione":True, "risultato":utente}
        
        except Exception as e:
            db.session.rollback()
            
            return {"operazione":False, "risultato":str(e)}
    
    # DELETE
    
    @staticmethod
    def delete(id_utente):
        try:
            utente = db.session.get(Utente, id_utente)
            if not utente:
                return {"operazione":False, "risultato":"Utente non trovato, impossibile completare l'operazione."}
    
            db.session.delete(utente)
            db.commit()

            return {"operazione":True, "risultato":utente}
        
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
    def create(id_libro, id_utente, data_inizio, data_fine):
        prestito = Prestito(id_libro, id_utente, data_inizio, data_fine)
        try:
            db.session.add(prestito)
            db.session.commit()
            
            return {"operazione":True, "risultato":prestito}

        except Exception as e:
            db.session.rollback()
            
            return {"operazione":False, "risultato":str(e)}
        
    # READ 
    
    @staticmethod
    def read_all():
        return db.session.query(Prestito).all()  
    
    @staticmethod
    def read_book_id(id_libro):
        return db.session.query(Prestito).filter_by(id_libro=id_libro).all()
    
    @staticmethod
    def read_user_id(id_utente):
        return db.session.query(Prestito).filter_by(id_utente=id_utente).first()
    
    # UPDATE
    
    @staticmethod
    def update(id_prestito, data_fine=None):
        try:
            prestito = db.session.get(Prestito, id_prestito)
            if not prestito:
                return {"operazione":False, "risultato":"Prestito non trovato, impossibile completare l'operazione."}
            
            if data_fine is not None:
                prestito.data_fine = data_fine
                
            db.session.commit()
    
            return {"operazione":True, "risultato":prestito}

        except Exception as e:
            db.session.rollback()
        
            return {"operazione":False, "risultato":str(e)}
        
    # DELETE
    
    @staticmethod
    def delete(id_prestito):
        try:
            prestito = db.session.get(Prestito, id_prestito)
            if not prestito:
                return {"operazione":False, "risultato":"Prestito non trovato, impossibie completare l'operazione."}
            
            db.session.delete(prestito)
            db.session.commit()
            
        except Exception as e:
            db.session.rollback()
            
            return {"operazione":False, "risultato":str(e)}
        
