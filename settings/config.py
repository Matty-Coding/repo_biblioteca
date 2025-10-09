from os import getcwd
from os.path import join

class Configurazione:
    SECRET_KEY = "supercalifragilistichespiralidoso"
    BASEDIR = getcwd()
    DATABASE_NAME = "Bibliooo.db"
    DATABASE_PATH = join(BASEDIR, DATABASE_NAME)
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
