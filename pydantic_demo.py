from pydantic import BaseModel , EmailStr , AnyUrl
from typing import List, Dict , Optional

class user(BaseModel):
    name: str
    age: int
    portfolio_url : Optional[AnyUrl] = None # this field is optional and can be None or a valid URL
    city: str
    email : EmailStr
    contact_details : Dict[str,str]  #we can also use directly in built types like dist[str,str] or list[str] or list[int] etc
    safety_questions_answers : Optional[List[str]] = None #now this field is optional and can be None or list of strings
    married : bool = False # this is default value field, if not provided it will be False
    

def insert_user_data(user_instance: user):
    # Here you can insert the user data into a database or perform any other operations
    print(user_instance)

# Example usage
user_data = {
    "name" : "Alice",
    "age" : 30,
    "city" : "New York",
    "email" : "alice@example.com",
    "portfolio_url" : "https://alice.example.com",
    "contact_details" : {
        "email" : "alice@example.com",
        "phone" : "123-456-7890"
    },
    "safety_questions_answers" : [
        "Yes",
        "No",
        "Maybe"
    ]
}

user_instance = user(**user_data)
insert_user_data(user_instance)