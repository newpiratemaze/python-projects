from pydantic import BaseModel

class PostBase(BaseModel):
    num: str


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int

    class Config:
        orm_mode = True


