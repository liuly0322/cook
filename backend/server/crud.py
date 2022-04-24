from sqlalchemy.orm import Session

from . import models, schemas

import datetime


def get_notes(db: Session):
    return db.query(models.Note).all()


def create_note(db: Session, note: schemas.NoteCreate):
    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    db_note = models.Note(description=note.description, create_time=now_time)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def delete_note(db: Session, id: int):
    db_note = db.query(models.Note).filter(models.Note.id == id).delete()
    db.commit()
    return db_note
