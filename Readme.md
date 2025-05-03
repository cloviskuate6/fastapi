# API REST FastAPI Items

Une API REST simple pour la gestion d'items, développée avec FastAPI et déployée automatiquement via CI/CD sur Render.

## Fonctionnalités

- CRUD complet pour la gestion des items (Create, Read, Update, Delete)
- Tests automatisés avec pytest
- Vérification de qualité du code avec flake8
- Pipeline CI/CD avec GitHub Actions
- Déploiement automatique sur Render

## Structure du projet

```
project/
├── app/                    # Code source de l'API
│   ├── __init__.py
│   ├── main.py             # Application principale FastAPI
│   └── models.py           # Modèles de données Pydantic
├── tests/                  # Tests unitaires
│   ├── __init__.py
│   └── test_main.py        # Tests pour l'API
├── .github/workflows/      # Configuration GitHub Actions
│   └── ci.yml              # Pipeline CI/CD
├── .flake8                 # Configuration flake8
├── .gitignore              # Fichiers à ignorer dans Git
├── render.yaml             # Configuration pour Render
├── requirements.txt        # Dépendances Python
└── README.md               # Documentation
```

## Installation en local

1. Cloner le dépôt:

   ```bash
   git clone https://github.com/votre-nom/fastapi-items-api.git
   cd fastapi-items-api
   ```

2. Créer un environnement virtuel:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows: venv\Scripts\activate
   ```

3. Installer les dépendances:

   ```bash
   pip install -r requirements.txt
   ```

4. Lancer l'API:

   ```bash
   uvicorn app.main:app --reload
   ```

5. Accéder à l'API:
   - API: http://localhost:8000
   - Documentation Swagger: http://localhost:8000/docs
   - Documentation ReDoc: http://localhost:8000/redoc

## Utilisation de l'API

### Liste des endpoints

| Méthode | URL         | Description                 |
| ------- | ----------- | --------------------------- |
| GET     | /           | Page d'accueil de l'API     |
| GET     | /items      | Liste tous les items        |
| GET     | /items/{id} | Récupère un item spécifique |
| POST    | /items      | Crée un nouvel item         |
| PUT     | /items/{id} | Met à jour un item existant |
| DELETE  | /items/{id} | Supprime un item            |

### Exemples de requêtes

#### Créer un item

```bash
curl -X POST "http://localhost:8000/items" -H "Content-Type: application/json" -d '{"name": "Produit Test", "price": 29.99, "in_stock": true}'
```

#### Récupérer tous les items

```bash
curl "http://localhost:8000/items"
```

#### Récupérer un item spécifique

```bash
curl "http://localhost:8000/items/1"
```

#### Mettre à jour un item

```bash
curl -X PUT "http://localhost:8000/items/1" -H "Content-Type: application/json" -d '{"name": "Produit Modifié", "price": 39.99}'
```

#### Supprimer un item

```bash
curl -X DELETE "http://localhost:8000/items/1"
```

## Tests

Exécuter les tests:

```bash
pytest
```

Exécuter les tests avec couverture:

```bash
pytest --cov=app tests/
```

## Linting

Vérifier la qualité du code:

```bash
flake8 .
```

## Déploiement

L'application est configurée pour se déployer automatiquement sur Render à chaque push sur la branche `main`.
