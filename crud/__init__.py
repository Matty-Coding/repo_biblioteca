# importo dai moduli della cartella 
from .crud_function import CRUD_Libro, CRUD_Utente, CRUD_Prestito

# rendo pubblico tutto quello importato
# in modo da usarlo comodamente importando la cartella
__all__ = ["CRUD_Libro", "CRUD_Utente", "CRUD_Prestito"]


