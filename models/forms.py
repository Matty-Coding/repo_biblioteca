
from flask_wtf import FlaskForm    # form di flask 
from wtforms import PasswordField, StringField, SubmitField    # classi con Field == type input HTML
from wtforms.validators import DataRequired as req, Email, Length, Regexp as reg     # controlli di validazione



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
    
    email = StringField("Email",
                        validators=[
                            req(), 
                            Email(), 
                            reg(r"^[a-zA-Z0-9]+[_.-]?[a-zA-Z0-9]+@[a-zA-Z0-9]+[-.]?[a-zA-Z0-9]+\.[a-zA-Z]{2,}$", 
                                message="Devi inserire una mail valida.")
                            ]
                        )
    
    telefono = StringField("Telefono",
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
                                    message="La password deve contenere almeno una maiuscola, minuscola, numero e simbolo tra ?.!_*")
                                ] 
                            )
    
    submit = SubmitField("Registrati")
    


class LoginForm(FlaskForm):
    utente = StringField(
        "Email o numero di telefono",
        validators=[
            req(),
            reg(r"^\d{10}$|^[a-zA-Z0-9]+[_.-]?[a-zA-Z0-9]+@[a-zA-Z0-9]+[-.]?[a-zA-Z0-9]+\.[a-zA-Z]{2,}$",
            message="Devi inserire un numero di telefono o una mail valida")            
        ]
            
    )
    
    password = PasswordField(
        "password",
        validators=[
            req(), 
            Length(min=8), 
            reg(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%&*?.])[^\-';\"$@].{8,}$",
                message="La password deve contenere almeno una maiuscola, minuscola, numero e simbolo tra ?.!_*")
            ] 
        )
    
    submit = SubmitField("Accedi")