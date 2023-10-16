import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from src.database import Base


class ProductDB(Base):
    __tablename__ = "product"

    product_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, index=True)
    description = Column(String)
    brand_id = Column(UUID(as_uuid=True))  # Foreign key to Brand


class BrandDB(Base):
    __tablename__ = "brand"

    brand_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String)
