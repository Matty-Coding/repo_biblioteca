
from flask_wtf import FlaskForm    
from wtforms import (
    PasswordField, 
    StringField, 
    SubmitField, 
    EmailField, 
    TelField, 
    HiddenField,
    IntegerField  # per la quantità dei libri, non prende l'int (?) --> da capire
)   
from wtforms.validators import (
    DataRequired as req, 
    Email, 
    Length, 
    Regexp as reg,
    ReadOnly
)     


class RegisterForm(FlaskForm):
    nome = StringField("Nome", 
                       render_kw={"placeholder":"Inserisci nome", "autofocus":True},
                       validators=[
                           req(),
                           reg(r"^[A-Za-z ]+$",
                              message="Solo lettere o spazi consentiti") 
                           ]  
                       )
    
    cognome = StringField("Cognome",
                          render_kw={"placeholder":"Inserisci cognome"},
                          validators=[
                            req(), 
                            reg(r"^[A-Za-z ]+$", 
                                message="Solo lettere o spazi consentiti")
                            ]
                          )
    
    email = EmailField("Email",
                        render_kw={"placeholder":"Inserisci email"},
                        validators=[
                           req(), 
                           Email(), 
                           reg(r"^[a-zA-Z0-9]+[_.-]?[a-zA-Z0-9]+@[a-zA-Z0-9]+[-.]?[a-zA-Z0-9]+\.[a-zA-Z]{2,}$", 
                                message="Devi inserire una mail valida.")
                            ]
                        )
    
    telefono = TelField("Telefono",
                        render_kw={"placeholder":"Inserisci telefono"},
                           validators=[
                               req(),
                               reg(r"^\d{10}$", 
                                   message="Il numero deve contenere 10 cifre")
                                ]
                            )
    
    password = PasswordField("Password",
                             render_kw={"placeholder":"Inserisci password"},
                             validators=[
                                req(), 
                                Length(min=8),
                                reg(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%&*?.])[^\-';\"$@].{8,}$",
                                    message="La password deve essere di almeno 8 caratteri e contenere almeno una maiuscola, minuscola, numero e simbolo tra [?.!_*]")
                                ] 
                            )
    
    submit = SubmitField("Registrati")
    


class LoginForm(FlaskForm):
    utente = StringField(
        "Utente",
        render_kw={"placeholder":"Inserisci email o telefono"},
        validators=[
            req(),
            reg(r"^\d{10}$|^[a-zA-Z0-9]+[_.-]?[a-zA-Z0-9]+@[a-zA-Z0-9]+[-.]?[a-zA-Z0-9]+\.[a-zA-Z]{2,}$",
            message="Devi inserire un numero di telefono o una mail valida")            
        ]
            
    )
    
    password = PasswordField(
        "Password",
        render_kw={"placeholder":"Inserisci password"},
        validators=[
            req(), 
            Length(min=8), 
            reg(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%&*?.])[^\-';\"$@].{8,}$",
                message="La password deve essere di almeno 8 caratteri e contenere almeno una maiuscola, minuscola, numero e simbolo tra ?.!_*")
            ] 
        )
    
    submit = SubmitField("Accedi")
    
    
    
class LibroForm(FlaskForm):
    autore = StringField(
        "Autore",
        render_kw={"placeholder":"Inserisci autore", "autofocus":True},
        validators=[
            req(),
            reg(r"^[a-zA-Z0-9]+[a-zA-Z0-9 '.]+$",
                message="Lettere, numeri, spazi e simboli ['.] consentiti")
        ]
    )
    
    titolo = StringField(
        "Titolo",
        render_kw={"placeholder":"Inserisci titolo"},
        validators=[
            req(),
            reg(r"^[a-zA-Z0-9]+[a-zA-Z0-9 ']+$",
                message="Lettere, numeri, spazi e apostrofi consentiti")
        ]
    )
    
    genere = StringField(
        "Genere",
        render_kw={"placeholder":"Inserisci genere"},
        validators=[
            req(),
            reg(r"^[a-zA-Z -]+$",
                message="Lettere, spazi e trattini consentiti")
        ]
    )
    
    totale_libri = StringField(
        "Totale libri",
        render_kw={"placeholder":"Inserisci disponibili"},
        validators=[
            req(),
            reg(r"^\d+$", message="Solo valori interi consentiti")
        ]
    )
    
    submit = SubmitField("Invia")
    
    
class ModificaLibroForm(FlaskForm):
    id = StringField(
        "ID",
        render_kw={"readonly":True}
    )
    
    autore = StringField(
        "Autore",
        render_kw={"autofocus":True},
        validators=[
            reg(r"^[a-zA-Z0-9]+[a-zA-Z0-9 '.]+$",
                message="Lettere, numeri, spazi e simboli ['.] consentiti")            
        ]
    )
    
    titolo = StringField(
        "Titolo",
        validators=[
            reg(r"^[a-zA-Z0-9]+[a-zA-Z0-9 ']+$",
                message="Lettere, numeri, spazi e apostrofi consentiti")            
        ]
    )
    
    genere = StringField(
        "Genere",
        validators=[
            reg(r"^[a-zA-Z -]+$",
                message="Lettere, numeri, spazi e trattini consentiti")            
        ]
    )
    
    totale_libri = StringField(
        "Disponibili",
        validators=[
            reg(r"^\d+$", message="Solo valori interi consentiti")
        ]
    )
    
    submit = SubmitField("Modifica")