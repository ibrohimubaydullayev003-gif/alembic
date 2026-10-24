from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import models

app = FastAPI(title="FastAPI Alembic Migration Demo")


@app.get("/")
def home():
    return {"message": "FastAPI + Alembic loyiha ishlayapti"}


@app.get("/users")
def list_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@app.post("/users")
def create_user(full_name: str, email: str, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.email == email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Bu email avval ro'yxatdan o'tgan")
    user = models.User(full_name=full_name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@app.get("/categories")
def list_categories(db: Session = Depends(get_db)):
    return db.query(models.Category).all()


@app.post("/categories")
def create_category(name: str, description: str | None = None, db: Session = Depends(get_db)):
    category = models.Category(name=name, description=description)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


@app.get("/products")
def list_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()


@app.post("/products")
def create_product(name: str, price: float, category_id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Kategoriya topilmadi")
    product = models.Product(name=name, price=price, category_id=category_id)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
