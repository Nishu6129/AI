from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: str

    @field_validator("username")
    def validate_username(cls, v):
        if " " in v:
            raise ValueError("Username cannot contain spaces")
        return v.lower()  # Normalize to lowercase

user = User(username="AliceSmith")
print(user.username)  # alicesmith