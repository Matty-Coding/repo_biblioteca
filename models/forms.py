
from flask_wtf import FlaskForm    
from wtforms import (
    PasswordField, 
    StringField, 
    SubmitField, 
    EmailField, 
    TelField, 
    IntegerField  # per la quantità dei libri, non prende l'int (?) --> da capire
)   
from wtforms.validators import (
    DataRequired as req, 
    Email, 
    Length, 
    Regexp as reg
)     


class RegisterForm(FlaskForm):
    nome = StringField("Nome", 
                       validators=[
                           req(),
                           reg(r"^[A-Za-z ]+$",
                              message="Solo lettere o spazi consentiti") 
                           ]  
                       )
    
    cognome = StringField("Cognome", 
                          validators=[
                            req(), 
                            reg(r"^[A-Za-z ]+$", 
                                message="Solo lettere o spazi consentiti")
                            ]
                          )
    
    email = EmailField("Email",
                        validators=[
                            req(), 
                            Email(), 
                            reg(r"^[a-zA-Z0-9]+[_.-]?[a-zA-Z0-9]+@[a-zA-Z0-9]+[-.]?[a-zA-Z0-9]+\.[a-zA-Z]{2,}$", 
                                message="Devi inserire una mail valida.")
                            ]
                        )
    
    telefono = TelField("Telefono",
                           validators=[
                               req(),
                               reg(r"^\d{10}$", 
                                   message="Il numero deve contenere 10 cifre")
                                ]
                            )
    
    password = PasswordField("Password",
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
        validators=[
            req(),
            reg(r"^\d{10}$|^[a-zA-Z0-9]+[_.-]?[a-zA-Z0-9]+@[a-zA-Z0-9]+[-.]?[a-zA-Z0-9]+\.[a-zA-Z]{2,}$",
            message="Devi inserire un numero di telefono o una mail valida")            
        ]
            
    )
    
    password = PasswordField(
        "Password",
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
        validators=[
            req(),
            reg(r"^[a-zA-Z0-9]+[a-zA-Z0-9 '.]+$",
                message="Lettere, numeri, spazi e simboli ['.] consentiti")
        ]
    )
    
    titolo = StringField(
        "Titolo",
        validators=[
            req(),
            reg(r"^[a-zA-Z0-9]+[a-zA-Z0-9 ']+$",
                message="Lettere, numeri, spazi e apostrofi consentiti")
        ]
    )
    
    genere = StringField(
        "Genere",
        validators=[
            req(),
            reg(r"^[a-zA-Z -]+$",
                message="Lettere, spazi e trattini consentiti")
        ]
    )
    
    totale_libri = StringField(
        "Totale libri",
        validators=[
            req(),
            reg(r"^\d+$", message="Solo valori interi consentiti")
        ]
    )
    
    submit = SubmitField("Invia")