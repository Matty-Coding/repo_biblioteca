# Applicazione Web per Gestire una Biblioteca

Questa applicazione permette di aggiungere, visualizzare, aggiornare ed eliminare libri da una biblioteca.

---

## Tecnologie e linguaggi usati

* **Git/GitHub:** Versionamento progressivo del codice
* **VirtualEnv:** Ambiente virtuale separato per il progetto
* **Python:** Sviluppo Back-end e gestione della logica applicativa
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
virtualenv nome_cartella

# Se necessario bypassare i permessi
powershell -ExecutionPolicy -Bypass

# Attivazione ambiente virtuale (Windows)
nome_cartella\Scripts\activate

# Installazione pacchetti
pip install nome_pacchetto

# Creazione requirements.txt
# Aggiornato ogni volta che si installano nuovi pacchetti
pip freeze > requirements.txt
```

### 4. Creazione struttura del progetto

```text
biblioteca/
├── templates/               # file HTML
│   ├── base.html
│   ├── index.html
│   ├── aggiungi_libro.html
│   └── modifica_libro.html
├── static/                  # file CSS e JS
│   ├── style.css
│   └── script.js
├── app.py                   # file principale Flask
└── requirements.txt         # dipendenze Python
```

---

## Uso dell'Applicazione

1. Attiva il virtualenv
2. Installa le dipendenze (`pip install -r requirements.txt`)
3. Avvia il server Flask (`python app.py`)
4. Apri il browser su `http://127.0.0.1:5000`

