
from os.path import exists
from flask import Flask, render_template, url_for, flash, redirect
from settings import Configurazione
from models import Libro, Utente, Prestito, db, RegisterForm, LoginForm, LibroForm, ModificaLibroForm
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
    return db.session.get(Utente, int(user_id))


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
            return render_template("login.html", form=form) 
        
        login_user(utente)

        # DEBUG
        if utente.is_authenticated:
            print(f"\n✅ {utente.nome.title()} {utente.cognome.title()} è autenticato correttamente.")
            
        flash("Accesso eseguito correttamente!", "success")
        return redirect(url_for("aggiungi_libro"))
               
    else:
        if form.errors:
            for errore in form.errors.values():
                flash(f"{errore}", "error")
            
    return render_template("login.html", form=form)


@app.route("/", methods=["GET", "POST"])
def index():
    # lettura di tutti i libri
    libri_disponibili = [libro.to_dict() for libro in CRUD_Libro.read_all()]

    return render_template("index.html", libri_disponibili=libri_disponibili)


@app.route("/aggiungi-libro", methods=["GET", "POST"])
@login_required
def aggiungi_libro():
    form = LibroForm()
    if form.validate_on_submit():
        libro = CRUD_Libro.create(
            autore = form.autore.data,
            titolo = form.titolo.data,
            genere = form.genere.data,
            totale_libri = form.totale_libri.data
        )

        if libro.get("risultato"):
            flash("Libro aggiunto correttamente", "success")
            return redirect(url_for("index"))

        else:
            flash("Non è stato possibile aggiungere il libro, riprovare", "error")
            return redirect(url_for("index"))
        
    else:
        if form.errors:
            for errore in form.errors.values():
                flash(f"{errore}", "error")

    return render_template("aggiungi_libro.html", form=form)


@app.route("/modifica-libro/<int:id>", methods=["GET", "POST"])
@login_required
def modifica_libro(id):
    # popola il form con i dati relativi al id inserito
    # li rende callable per poterli richiamare tramite jinja2 in html
    libro_esistente = CRUD_Libro.read_id(id)
    form = ModificaLibroForm(obj=libro_esistente)
    print("\nLIBRO ESISTENTE --> ", form.data)
    if form.validate_on_submit():
        libro_modificato = CRUD_Libro.update(
            id_libro = form.id.data,
            autore = form.autore.data,
            titolo = form.titolo.data,
            genere = form.genere.data,
            totale_libri = form.totale_libri.data
        )

        if libro_modificato.get("risultato"):
            flash("Libro modificato correttamente", "success")
            return redirect(url_for("index"))
        
        else:
            flash("Non è stato possibile modificare il libro, riprovare", "error")
            return redirect(url_for("index"))
        
    else:
        if form.errors:
            for errore in form.errors.values():
                flash(f"{errore}", "error")
        
    return render_template("modifica_libro.html", form=form, id=id)



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
                
    app.run(debug=True)