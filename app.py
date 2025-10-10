
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

# Route Home Page
@app.route("/")
def index():
    return render_template("index.html")




if __name__ == "__main__":
    with app.app_context():
        try:
            if exists(Configurazione.DATABASE_PATH):
                print(f"\n✅ Database già esistente nella directory.\nPath Database --> {Configurazione.DATABASE_PATH}")
            else:
                db.create_all()
                print(f"\n✅ Database creato correttamente.\nPath Database --> {Configurazione.DATABASE_PATH}")
                
        except Exception as e:
            print(f"\n⚠️  Non è stato possibile creare il database.\n{str(e)}")
                
    app.run(debug=True)