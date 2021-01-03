from typing import Optional, List
from fastapi import FastAPI, Depends
import sqlite3
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# get all books
@app.get("/", response_model=List[schemas.Book])
def read_books(db: Session = Depends(get_db)):
    books = crud.get_all_books(db)

    return books

# for testing
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
