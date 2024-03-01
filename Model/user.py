from Model.base_model import BaseModel

class User(BaseModel):
    id:int
    username:str
    email:str
    password:str

    def __init__(self, id:int, username:str, email:str, password:str) -> None:
        super().__init__(id=id,username=username,email=email,password=password)

    @staticmethod
    def from_dict(data: dict):
        return User(data['id'],data['username'],data['email'],data['password'])
    
    @staticmethod
    def __from_tuple(data: tuple):
        return User(data[0],data[1],data[2],data[3])
    
    @staticmethod
    def create(username:str,email:str,password:str)-> 'User':
        res = BaseModel.create(User,username=username,email=email,password=password)
        if res:
            return User.__from_tuple(res)
    
    @staticmethod
    def read(**kwargs)-> list['User']:
        res = BaseModel.read(User,**kwargs)
        if res:
            return [User.__from_tuple(row) for row in res]
        return []
    
    def delete(self):
        super().delete()