# Architecture Python - GestionPro

## Structure du projet

```
gestionpro/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Point d'entrée FastAPI
│   ├── config.py              # Configuration de l'application
│   ├── database.py            # Configuration base de données
│   ├── models/                # Modèles SQLAlchemy
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── client.py
│   │   ├── vehicle.py
│   │   ├── quote.py
│   │   └── alert.py
│   ├── schemas/               # Schémas Pydantic
│   │   ├── __init__.py
│   │   ├── client.py
│   │   ├── vehicle.py
│   │   ├── quote.py
│   │   └── alert.py
│   ├── crud/                  # Opérations CRUD
│   │   ├── __init__.py
│   │   ├── client.py
│   │   ├── vehicle.py
│   │   ├── quote.py
│   │   └── alert.py
│   ├── api/                   # Routes API
│   │   ├── __init__.py
│   │   ├── deps.py            # Dépendances
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── clients.py
│   │   │   ├── vehicles.py
│   │   │   ├── quotes.py
│   │   │   ├── alerts.py
│   │   │   └── dashboard.py
│   ├── services/              # Logique métier
│   │   ├── __init__.py
│   │   ├── client_service.py
│   │   ├── vehicle_service.py
│   │   ├── quote_service.py
│   │   ├── alert_service.py
│   │   └── dashboard_service.py
│   ├── utils/                 # Utilitaires
│   │   ├── __init__.py
│   │   ├── email.py
│   │   ├── pdf.py
│   │   └── notifications.py
│   └── frontend/              # Interface utilisateur
│       ├── __init__.py
│       ├── main.py            # Streamlit app
│       ├── components/
│       │   ├── __init__.py
│       │   ├── dashboard.py
│       │   ├── clients.py
│       │   ├── vehicles.py
│       │   ├── quotes.py
│       │   └── alerts.py
│       └── utils/
│           ├── __init__.py
│           ├── auth.py
│           └── helpers.py
├── tests/                     # Tests
│   ├── __init__.py
│   ├── test_clients.py
│   ├── test_vehicles.py
│   ├── test_quotes.py
│   └── test_alerts.py
├── migrations/                # Migrations Alembic
├── static/                    # Fichiers statiques
├── templates/                 # Templates HTML (si nécessaire)
├── requirements.txt           # Dépendances Python
├── .env                       # Variables d'environnement
├── .gitignore
├── README.md
└── docker-compose.yml         # Configuration Docker
```

## Technologies recommandées

### Backend (API)
- **FastAPI** : Framework web moderne et rapide
- **SQLAlchemy** : ORM pour la base de données
- **Pydantic** : Validation des données
- **Alembic** : Migrations de base de données
- **PostgreSQL** : Base de données principale
- **Redis** : Cache et sessions

### Frontend
- **Streamlit** : Interface utilisateur interactive
- **Plotly** : Graphiques et visualisations
- **Pandas** : Manipulation des données

### Utilitaires
- **Celery** : Tâches asynchrones
- **pytest** : Tests
- **Black** : Formatage du code
- **Flake8** : Linting

## Commandes de démarrage

```bash
# Installation des dépendances
pip install -r requirements.txt

# Démarrage de l'API
uvicorn app.main:app --reload --port 8000

# Démarrage du frontend
streamlit run app/frontend/main.py --server.port 8501

# Démarrage avec Docker
docker-compose up -d
```

## Configuration des variables d'environnement

```env
# .env
DATABASE_URL=postgresql://user:password@localhost/gestionpro
REDIS_URL=redis://localhost:6379
SECRET_KEY=your-secret-key
ENVIRONMENT=development
```

## Avantages de cette architecture

1. **Séparation des responsabilités** : API et frontend séparés
2. **Scalabilité** : Composants modulaires et réutilisables
3. **Testabilité** : Structure claire pour les tests
4. **Maintenabilité** : Code organisé et documenté
5. **Performance** : Utilisation de FastAPI et Redis
6. **Flexibilité** : Possibilité d'ajouter d'autres frontends