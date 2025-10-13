# Applicazione Web per Gestire una Biblioteca

Questa applicazione permette di effettuare operazioni CRUD (Create, Read, Update, Delete) su una biblioteca.

---

## Tecnologie e linguaggi usati

* **Git/GitHub:** Versionamento progressivo del codice
* **VirtualEnv:** Ambiente virtuale separato per il progetto
* **Python (3.13.0):** Sviluppo Back-end e gestione della logica applicativa
* **SQL/SQLAlchemy:** Database relazionale
* **Flask:** Server web e routing
* **Jinja2:** Inserimento di variabili Python nei template HTML
* **HTML:** Struttura delle pagine web
* **CSS:** Personalizzazione dei template HTML
* **JavaScript:** Gestione delle interazioni utente

---

## Inizializzazione del Progetto

### 1. Creazione Repository GitHub

1. Crea il repository su GitHub
2. Copia il link del repository

### 2. Collegamento cartella di lavoro al repository tramite Git

```bash
cd path_cartella
git init
git remote add origin <link_repo>
git branch -M main
git add primo_file.estensione
git commit -m "first commit"
git status
git push -u origin main
```

### 3. Creazione VirtualEnvironment

```bash
# Creazione ambiente virtuale
virtualenv <nome_cartella>

# Attivazione ambiente virtuale (Windows)
nome_cartella\Scripts\activate

# Installazione pacchetti
pip install <nome_pacchetto>

# Creazione requirements.txt
# Aggiornato ogni volta che si installano nuovi pacchetti
pip freeze --version > requirements.txt
```

### 4. Creazione struttura del progetto

```text
├── crud/
|    ├── __init__.py
|    └── crud_function.py
├── models/
|    ├── __init__.py
|    └── object_model.py
├── settings/
|    ├── __init__.py
|    └── config.py
├── static/
|    └── style.css
├── templates/
|   ├── aggiungi_libro.html
|   ├── base.html
|   ├── index.html
|   └── modifica_lìbro.html
├── app.py
└── requirements.txt
```

---

## Sviluppo dell'applicazione

Il progetto è stato suddiviso in tante sezioni, tutte comunicanti tra di loro. <br>

---

`SQLAlchemy` interagisce con il Database scrivendo codice Python, questo esclude la presenza di query `SQL` esplicite. <br>

Crea un ponte di comunicazione con il Database in questo modo:

```text
Codice Python --> SQLAlchemy crea una query in SQL --> Comunica con il database
```

---

`Flask` si occupa della gestione del Server e di tutto ciò che si collega ad esso. <br>
Una delle funzionalità più importanti è resa possibile da `Jinja2`, che permette di scrivere variabili e logiche di Python nelle pagine HTML.

---

`os` utile per gestire i PATH necessari all'app per funzionare.

---

Nelle varie sottocartelle o <i>"pacchetti"</i>, il flusso di lavoro viene gestito tramite delle Classi che contengono tutti i metodi necessari al funzionamento del progetto, facilitando l'importazione di quest'ultimi tra i vari file. <br>
I metodi sono implementati, dove necessario, con `Type Hinting` incluso per una migliore lettura e riutilizzo.

---

# Work in progress...

## Uso dell'Applicazione

1. Copia il repo con il comando: `Git clone https://github.com/Matty-Coding/repo_biblioteca`
2. Crea e attiva un virtualenv
3. Installa le dipendenze con il comando: `pip install -r requirements.txt`
4. Avvia il server Flask con il comando: `python app.py`
5. Apri il browser su `http://127.0.0.1:5000`


