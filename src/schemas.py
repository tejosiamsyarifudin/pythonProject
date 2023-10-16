from pydantic import BaseModel, UUID4


# Pydantic model for the product
class ProductBase(BaseModel):
    name: str
    description: str | None = None
    brand_id: UUID4


class ProductCreate(ProductBase):
    pass


class Product(ProductCreate):
    product_id: UUID4

    class Config:
        orm_mode = True


# Pydantic model for the brand
class BrandBase(BaseModel):
    Name: str


class BrandCreate(BrandBase):
    pass


class Brand(BrandCreate):
    brand_id: UUID4

    class Config:
        orm_mode = True
