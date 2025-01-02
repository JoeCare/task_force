from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    """Serializerused for data validation when creating a new user excluding vars ssigned by DB.
    """
    email: EmailStr
    username: str
    password: str

class UserResponse(BaseModel):
    """Serializer of the client response excluding sensitive data. """
    email: EmailStr
    username: str

class UserLogin(BaseModel):
    """Serializer of login credentials."""
    email: EmailStr
    password: str

