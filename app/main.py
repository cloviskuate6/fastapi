from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, HTTPException, status
from typing import List, Dict
from .models import Item, ItemCreate, ItemUpdate

app = FastAPI(
    title="Items API", description="API pour gérer des items", version="1.0.0"
)

# Base de données simple en mémoire
items_db: Dict[int, Item] = {}
counter = 1

# Monter le dossier 'static' pour accéder à l'image
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <html>
        <head>
            <title>Accueil API Items</title>
            <style>
                body {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    font-family: Arial, sans-serif;
                }
                h1 {
                    font-weight: bold;
                }
                img {
                    max-width: 300px;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <h1><strong>Bienvenue sur l'API Items</strong></h1>
            <img src="/static/logo.jpeg" alt="Logo de l'API">
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/items", response_model=List[Item])
def get_items():
    """Récupère la liste de tous les items."""
    return list(items_db.values())


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    """Récupère un item spécifique par son ID."""
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item avec l'ID {item_id} non trouvé",
        )
    return items_db[item_id]


@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate):
    """Crée un nouvel item."""
    global counter
    new_item = Item(
        id=counter, name=item.name, price=item.price, in_stock=item.in_stock
    )
    items_db[counter] = new_item
    counter += 1
    return new_item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item_update: ItemUpdate):
    """Met à jour un item existant."""
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item avec l'ID {item_id} non trouvé",
        )

    stored_item = items_db[item_id]
    update_data = item_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(stored_item, field, value)

    items_db[item_id] = stored_item
    return stored_item


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    """Supprime un item."""
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item avec l'ID {item_id} non trouvé",
        )

    del items_db[item_id]
    return None


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
