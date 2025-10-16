from os import getenv, getcwd
from os.path import join
from dotenv import load_dotenv

load_dotenv()

class Configurazione:
    SECRET_KEY = getenv("SECRET_KEY", "chiavesupersegreta")
    DATABASE_PATH = join(getcwd(), "Bibliooo.db")
    SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)


