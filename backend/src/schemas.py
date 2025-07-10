from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str = "user"


class ReadUser(CreateUser):
    id: int

    model_config = {
        "from_attributes": True
    }
