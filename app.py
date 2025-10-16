
from os.path import exists
from flask import Flask, render_template, url_for, flash, redirect
from settings import Configurazione
from models import Libro, Utente, Prestito, db, RegisterForm, LoginForm, LibroForm
from crud import CRUD_Libro, CRUD_Utente, CRUD_Prestito
from flask_login import login_required, LoginManager, login_user, logout_user, current_user



# Istanza della Classe Flask + definizione path static/template
app = Flask(__name__)

# Collego la configurazione all'app, incluso il path del Database
app.config.from_object(Configurazione)

# Inizializzazione del database connesso all'app
db.init_app(app)

# Istanzio l'oggetto login_manager dalla classe importata LoginManager
login_manager = LoginManager()

# lo collego e inizializzo all'app
login_manager.init_app(app)

# carico utente
@login_manager.user_loader
def load_user(user_id):
    return db.session(Utente, int(user_id))


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()    
    if form.validate_on_submit():
        if not CRUD_Utente.read_email(form.email.data) and not CRUD_Utente.read_phone(form.telefono.data):
            CRUD_Utente.create(
                nome=form.nome.data,
                cognome=form.cognome.data,
                email=form.email.data,
                telefono=form.telefono.data,
                password=form.password.data
            )
            
            flash("Registrazione avvenuta correttamente.", "success")
            
            # return render_template("index.html")
            return redirect(url_for("login"))
        
        else:
            flash("Email o telefono già esistenti.", "error")
            
    else:
        if form.errors:
            for errori in form.errors.values():
                for errore in errori:
                    flash(f"{errore}", "error")
        
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if "@" in form.utente.data:
            utente = CRUD_Utente.read_email(form.utente.data)      
        else:
            utente = CRUD_Utente.read_phone(form.utente.data)   
            
        if not utente:
            flash("Utente non trovato. Riprovare", "warning")
            return render_template("login.html", form=form)  
        
        if not utente.verifica_password(form.password.data):
            flash("Credenziali errate. Accesso negato!", "error")
        
        login_user(utente)
        load_user(utente.id)

        # DEBUG
        if utente.is_authenticated:
            print(f"\n✅ {utente.nome.title()} {utente.cognome.title()} è autenticato correttamente.")
            
        flash("Accesso eseguito correttamente!", "success")
        return render_template("index.html")
               
    else:
        if form.errors:
            for errore in form.errors.values():
                flash(f"{errore}", "error")
            
    return render_template("login.html", form=form)


@app.route("/", methods=["GET", "POST"])
def index():
    # lettura di tutti i libri
    libri_disponibili = CRUD_Libro.read_all() 
    print("\n======== LIBRI DISPONIBILI =========\n", libri_disponibili)
    # gestione form get/post
    form = LibroForm()
    if form.validate_on_submit():
        libro = CRUD_Libro.create(
            autore = form.autore.data,
            titolo = form.titolo.data,
            genere = form.genere.data,
            totale_libri = form.totale_libri.data
        )

        nuovo_libro = libro.get("risultato")

        if nuovo_libro is not None:
            flash("Libro aggiunto correttamente", "success")
            return render_template("index.html", nuovo_libro=nuovo_libro, form=form)

        else:
            flash("Non è stato possibile aggiungere il libro, riprovare", "error")
            return render_template("index.html", form=form)
        
    else:
        if form.errors:
            for errore in form.errors.values():
                flash(f"{errore}", "error")
        
    return render_template("index.html", libri_disponibili=libri_disponibili, form=form)




if __name__ == "__main__":
    with app.app_context():
        try:
            if not exists(Configurazione.DATABASE_PATH):
                db.create_all()
                print(f"\n✅ Database creato correttamente.\nPath Database --> {Configurazione.SQLALCHEMY_DATABASE_URI}")

            else:
                print(f"\n✅ Database già esistente nella directory.\nPath Database --> {Configurazione.SQLALCHEMY_DATABASE_URI}")
            
        except Exception as e:
            print(f"\n⚠️  Non è stato possibile creare il database.\n{str(e)}")
                
    app.run(debug=True, host="0.0.0.0")