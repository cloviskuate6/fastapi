from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# def test_read_root():
# """Test l'endpoint racine."""
# response = client.get("/")
# assert response.status_code == 200
# assert response.json() == {"message": "Bienvenue sur l'API Items"}


def test_get_items_empty():
    """Test la récupération d'une liste vide d'items."""
    # Vider la base de données avant le test
    app.items_db = {}
    app.counter = 1
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []


def test_create_item():
    """Test la création d'un item."""
    # Vider la base de données avant le test
    app.items_db = {}
    app.counter = 1
    item_data = {"name": "Test Item", "price": 9.99, "in_stock": True}

    response = client.post("/items", json=item_data)
    assert response.status_code == 201
    created_item = response.json()
    assert created_item["id"] == 1
    assert created_item["name"] == item_data["name"]
    assert created_item["price"] == item_data["price"]
    assert created_item["in_stock"] == item_data["in_stock"]


def test_get_item():
    """Test la récupération d'un item spécifique."""
    # Vider la base de données avant le test
    app.items_db = {}
    app.counter = 1

    # Créer un item d'abord
    item_data = {"name": "Test Item", "price": 9.99, "in_stock": True}
    create_response = client.post("/items", json=item_data)
    item_id = create_response.json()["id"]

    # Récupérer l'item
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {
        "id": item_id,
        "name": item_data["name"],
        "price": item_data["price"],
        "in_stock": item_data["in_stock"],
    }


def test_get_item_not_found():
    """Test la récupération d'un item qui n'existe pas."""
    response = client.get("/items/999")
    assert response.status_code == 404
    assert "non trouvé" in response.json()["detail"]


def test_update_item():
    """Test la mise à jour d'un item."""
    # Vider la base de données avant le test
    app.items_db = {}
    app.counter = 1

    # Créer un item d'abord
    item_data = {"name": "Test Item", "price": 9.99, "in_stock": True}
    create_response = client.post("/items", json=item_data)
    item_id = create_response.json()["id"]

    # Mettre à jour l'item
    update_data = {"name": "Updated Item", "price": 19.99}
    response = client.put(f"/items/{item_id}", json=update_data)
    assert response.status_code == 200
    updated_item = response.json()
    assert updated_item["id"] == item_id
    assert updated_item["name"] == update_data["name"]
    assert updated_item["price"] == update_data["price"]
    assert updated_item["in_stock"] == item_data["in_stock"]  # Non modifié


def test_update_item_not_found():
    """Test la mise à jour d'un item qui n'existe pas."""
    update_data = {"name": "Test"}
    response = client.put("/items/999", json=update_data)
    assert response.status_code == 404
    assert "non trouvé" in response.json()["detail"]


def test_delete_item():
    """Test la suppression d'un item."""
    # Vider la base de données avant le test
    app.items_db = {}
    app.counter = 1

    # Créer un item d'abord
    item_data = {"name": "Test Item", "price": 9.99, "in_stock": True}
    create_response = client.post("/items", json=item_data)
    item_id = create_response.json()["id"]

    # Supprimer l'item
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 204

    # Vérifier que l'item a bien été supprimé
    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 404


def test_delete_item_not_found():
    """Test la suppression d'un item qui n'existe pas."""
    response = client.delete("/items/999")
    assert response.status_code == 404
    assert "non trouvé" in response.json()["detail"]
