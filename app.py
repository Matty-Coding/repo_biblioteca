
from os.path import exists
from flask import Flask, render_template
from settings import Configurazione
from models import Libro, Utente, Prestito, db
# from models.object_model import db
from crud import CRUD_Libro, CRUD_Utente, CRUD_Prestito


# Istanza della Classe Flask + definizione path static/template
app = Flask(__name__, static_folder="static", template_folder="templates")

# Collego la configurazione all'app, incluso il path del Database
app.config.from_object(Configurazione)

# Inizializzazione del database connesso all'app
db.init_app(app)

def login_required():
    def wrapper(*args, **kwarsg):
        pass
    
    return wrapper







# Route Home Page
@app.route("/")
def index():
    return render_template("index.html", route="/")




if __name__ == "__main__":
    with app.app_context():
        try:
            if not exists(Configurazione.DATABASE_PATH):
                print(f"\n✅ Database già esistente nella directory.\nPath Database --> {Configurazione.DATABASE_PATH}")
            else:
                db.create_all()
                print(f"\n✅ Database creato correttamente.\nPath Database --> {Configurazione.DATABASE_PATH}")
                
            # print("\n\n====== DEBUG ========\n\n")
            
            # print("=== TEST CRUD_LIBRO ===")
            # try:
            #     result = CRUD_Libro.create("Autore", "Titolo", "Genere", 3)
            #     print("CREATE Libro:", result)
                
            #     result = CRUD_Libro.read_all()
            #     print("READ ALL Libri:", [l.to_dict() for l in result])
                
            #     result = CRUD_Libro.read_id(1)
            #     print("READ ID 1 Libro:", result.to_dict() if result else None)
                
            #     result = CRUD_Libro.read_title("Titolo")
            #     print("READ Titolo 'Titolo':", result.to_dict() if result else None)
                
            #     result = CRUD_Libro.read_author("Autore")
            #     print("READ Autore 'Autore':", [l.to_dict() for l in result])
                
            #     result = CRUD_Libro.read_genre("Genere")
            #     print("READ Genere 'Genere':", [l.to_dict() for l in result])
                
            #     result = CRUD_Libro.update(1, titolo="Nuovo Titolo")
            #     print("UPDATE Titolo Libro ID 1:", result)
                
            #     result = CRUD_Libro.delete(1)
            #     print("DELETE Libro ID 1:", result)
            # except Exception as e:
            #     print(f"Errore CRUD_Libro: {e}")
            
            # print("\n=== TEST CRUD_UTENTE ===")
            # try:
            #     result = CRUD_Utente.create("Mario", "Rossi", "mario@rossi.it", "1234567890", "provapassword")
            #     print("CREATE Utente:", result)
                
            #     result = CRUD_Utente.read_all()
            #     print("READ ALL Utenti:", [u.to_dict() for u in result])
                
            #     result = CRUD_Utente.read_id(1)
            #     print("READ ID 1 Utente:", result.to_dict() if result else None)
                
            #     result = CRUD_Utente.read_name("Mario")
            #     print("READ Nome 'Mario':", [u.to_dict() for u in result])
                
            #     result = CRUD_Utente.read_surname("Rossi")
            #     print("READ Cognome 'Rossi':", [u.to_dict() for u in result])
                
            #     result = CRUD_Utente.read_email("mario@rossi.it")
            #     print("READ Email 'mario@rossi.it':", result.to_dict() if result else None)
                
            #     result = CRUD_Utente.read_phone("1234567890")
            #     print("READ Telefono '1234567890':", result.to_dict() if result else None)
                
            #     result = CRUD_Utente.update(1, nome="Luigi")
            #     print("UPDATE Nome Utente ID 1:", result)
                
            #     result = CRUD_Utente.delete(1)
            #     print("DELETE Utente ID 1:", result)
            # except Exception as e:
            #     print(f"Errore CRUD_Utente: {e}")
            
            # print("\n=== TEST CRUD_PRESTITO ===")
            # try:
            #     result = CRUD_Prestito.create(1, 1, "01/10/25", "15/10/25")
            #     print("CREATE Prestito:", result)
                
            #     result = CRUD_Prestito.read_all()
            #     print("READ ALL Prestiti:", [p.to_dict() for p in result])
                
            #     result = CRUD_Prestito.read_book_id(1)
            #     print("READ Prestiti Libro ID 1:", [p.to_dict() for p in result])
                
            #     result = CRUD_Prestito.read_user_id(1)
            #     print("READ Prestito Utente ID 1:", result.to_dict() if result else None)
                
            #     result = CRUD_Prestito.update(1, data_fine="20/10/25")
            #     print("UPDATE Data Fine Prestito ID 1:", result)
                
            #     result = CRUD_Prestito.delete(1)
            #     print("DELETE Prestito ID 1:", result)
            # except Exception as e:
            #     print(f"Errore CRUD_Prestito: {e}")
            
        except Exception as e:
            print(f"\n⚠️  Non è stato possibile creare il database.\n{str(e)}")
                
    app.run(debug=True)