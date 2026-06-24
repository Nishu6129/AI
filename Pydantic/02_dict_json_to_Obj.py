from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int

# Data from an API response
data = {"name": "Alice", "email": "alice@example.com", "age": 30}

# Option 1: Unpack the dict (simple, common)
user1 = User(**data)
print(user1)

# Option 2: Use model_validate (explicit, more options)
user = User.model_validate(data)
print(user)