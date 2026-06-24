from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str
    star: int  | None = None

user = User(name="Alice", age="30", email="alice@example.com", star="12")
print(user)

user_dict = user.model_dump() # Convert the User instance to a dictionary
print(user_dict)

user_json = user.model_dump_json() # Convert the User instance to a JSON string
print(user_json)

# from dataclasses import dataclass

# @dataclass
# class User:
#     name: str
#     email: str
#     age: int

# user = User(name="Alice", email="alice@example.com", age="not a number")
# print(user.age)  # "not a number" - no validation!  it will work give only comment but it will not raise an error.



