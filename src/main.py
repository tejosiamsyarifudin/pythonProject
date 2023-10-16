from fastapi import Depends, FastAPI, status
from pydantic import UUID4
from sqlalchemy.orm import Session
from src import models
from src.schemas import ProductCreate, Product
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create a product
@app.post("/products/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = models.ProductDB(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# Read a single product
@app.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: UUID4, db: Session = Depends(get_db)):
    db_product = db.query(models.ProductDB).filter(models.ProductDB.product_id == product_id).first()
    return db_product


# Update a product
@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: UUID4, product: ProductCreate, db: Session = Depends(get_db)):
    db_product = db.query(models.ProductDB).filter(models.ProductDB.product_id == product_id).first()
    for key, value in product.dict().items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product


# Delete a product
@app.delete("/products/{product_id}", response_model=Product)
async def delete_product(product_id: UUID4, db: Session = Depends(get_db)):
    db_product = db.query(models.ProductDB).filter(models.ProductDB.product_id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product


# List all products
@app.get("/products/", response_model=list[Product])
async def read_product(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_product = db.query(models.ProductDB).offset(skip).limit(limit).all()
    return db_product
