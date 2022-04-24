from pydantic import BaseModel


class NoteBase(BaseModel):
    description: str


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    id: int
    create_time: str

    class Config:
        orm_mode = True
