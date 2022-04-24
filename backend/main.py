from typing import List

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

import server.crud as crud
import server.models as models
import server.schemas as schemas
from server.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"],
                   allow_headers=["*"],)

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/notes", response_model=List[schemas.Note])
def read_notes(db: Session = Depends(get_db)):
    notes = crud.get_notes(db)
    return notes


@app.post("/notes")
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    return crud.create_note(db, note)


@app.delete("/notes")
def delete_note(id: int, db: Session = Depends(get_db)):
    return crud.delete_note(db, id)
