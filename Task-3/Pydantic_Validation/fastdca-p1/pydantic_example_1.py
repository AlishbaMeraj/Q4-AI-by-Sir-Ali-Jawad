from pydantic import BaseModel, ValidationError

# Define a simple model
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None  # Optional field with default None

# Valid data
user_data = {"id": 1,
             "name": "Fatima", 
             "email": "fatimanazeer488@gmail.com",
             "age": 55}
user = User(**user_data)
print(user)  
print(user.model_dump())  

# Invalid data (will raise an error)
try:
    invalid_user = User(id="not_an_int", name="Bob", email="bob@example.com")
except ValidationError as e:
    print(e)