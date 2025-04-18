# filepath: c:\Users\harie\dbapi\schemas.py
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    content: str