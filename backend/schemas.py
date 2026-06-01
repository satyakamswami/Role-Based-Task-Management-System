from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    role: str

    class Config:
        from_attributes = True

class TaskBase(BaseModel):
    title: str
    description: str

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str