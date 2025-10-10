# importo dai moduli della cartella 
from .object_model import Libro, Utente, Prestito, db

# rendo pubblico tutto quello importato
# in modo da usarlo comodamente importando la cartella
__all__ = ["Libro", "Utente", "Prestito", "db"]