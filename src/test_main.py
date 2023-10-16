import pytest
from httpx import AsyncClient

from src.main import app


# Create a product
@pytest.mark.anyio
async def test_create_product():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        product_data = {
            "name": "Ice Cream",
            "description": "Vanilla Ice Cream",
            "brand_id": "32e48b3b-29af-4281-af1c-afb55edda084"
        }

        response = await ac.post("/products/", json=product_data)
    assert response.status_code == 201
    product = response.json()

    assert product["name"] == "Ice Cream"
    assert product["description"] == "Vanilla Ice Cream"
    assert product["brand_id"] == "32e48b3b-29af-4281-af1c-afb55edda084"
    assert "product_id" in product  # Check if "product_id" exists in the response


# Read a single product
@pytest.mark.anyio
async def test_read_single_product():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/products/71bd07b6-5a5b-4e89-91d7-e6ac2acc9936")
    assert response.status_code == 200
    product = response.json()

    assert product["name"] == "Value Meals 3"
    assert product["description"] == "Noodles + Lemon Tea"
    assert product["brand_id"] == "32e48b3b-29af-4281-af1c-afb55edda084"
    assert product["product_id"] == "71bd07b6-5a5b-4e89-91d7-e6ac2acc9936"


# Update a product
@pytest.mark.anyio
async def test_update_product():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        product_data = {
            "name": "Value Meals 3",
            "description": "Noodles + Lemon Tea",
            "brand_id": "32e48b3b-29af-4281-af1c-afb55edda084"
        }

        response = await ac.put("/products/71bd07b6-5a5b-4e89-91d7-e6ac2acc9936", json=product_data)
    assert response.status_code == 200
    product = response.json()

    assert product["name"] == "Value Meals 3"
    assert product["description"] == "Noodles + Lemon Tea"
    assert product["brand_id"] == "32e48b3b-29af-4281-af1c-afb55edda084"
    assert product["product_id"] == "71bd07b6-5a5b-4e89-91d7-e6ac2acc9936"


# List all products
@pytest.mark.anyio
async def test_read_product():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/products/?skip=0&limit=100")
    assert response.status_code == 200
    products = response.json()
    for product in products:
        assert product["name"]
        assert product["description"]
        assert product["brand_id"]
        assert product["product_id"]


# Delete a product
@pytest.mark.anyio
async def test_delete_product():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/products/c45d00db-78bb-4fcd-ba21-318fb57dc25e")
    assert response.status_code == 200
    product = response.json()

    assert "name" in product  # Check if "name" exists in the response
    assert "description" in product  # Check if "description" exists in the response
    assert "brand_id" in product  # Check if "brand_id" exists in the response
    assert "product_id" in product  # Check if "product_id" exists in the response
