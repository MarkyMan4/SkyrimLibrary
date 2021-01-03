# methods to create, read, update and delete from the database

from sqlalchemy.orm import Session
import models


def get_all_books(db: Session):
    return db.query(models.Book).all()
