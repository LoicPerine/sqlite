from dataclasses import dataclass
from typing import Optional

from Model.BaseModel import BaseModel

@dataclass
class Book(BaseModel):
    id:int
    title:str
    content:str
    publication_year:int
    author: str

    def __init__(self, id:int, title:str,author :str, content:str, publication_year:int) -> None:
        super().__init__(id=id,title=title,author=author,content=content,publication_year=publication_year)

    @staticmethod
    def from_dict(data: dict):
        return Book(data['id'],data['name'],data["author"],data['content'],data['publication_year'])
    @staticmethod
    def __from_tuple(data: tuple):
        return Book(data[0],data[1],data[2],data[3],data[4])
    
    @staticmethod
    def create(title:str,author:str,content:str, publication_year:int)-> Optional['Book']:
        res = BaseModel.create(Book,title=title,author=author,content=content,publication_year=publication_year)
        if res:
            return Book.__from_tuple(res)
    
    """
    this can be used to pass complex conditions, e.g.:
    Book.read(id__gt=1, publication_year__lt=2000) would return all books with id > 1 and publication_year < 2000
    """
    @staticmethod
    def read(**kwargs)-> list['Book']:
        res = BaseModel.read(Book,**kwargs)
        if res:
            return [Book.__from_tuple(row) for row in res]
        return []
    
    def delete(self):
        super().delete()
