from dataclasses import dataclass


@dataclass
class Book:
    id:int
    name:str
    content:str
    publication_year:int

    def __init__(self,id:int,name:str,content:str, publication_year:int):
        