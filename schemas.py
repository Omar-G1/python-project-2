from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List

# ============================================
# USER SCHEMAS
# ============================================

class UserCreate(BaseModel):
    """Schema for user signup"""
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8)

    class Config:
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "password": "securepass123"
            }
        }


class UserLogin(BaseModel):
    """Schema for user login"""
    username: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "password": "securepass123"
            }
        }


class UserResponse(BaseModel):
    """Schema for user response"""
    id: int
    username: str
    created_at: datetime

    class Config:
        from_attributes = True


# ============================================
# TASK SCHEMAS
# ============================================

class TaskCreate(BaseModel):
    """Schema for creating a task"""
    name: str = Field(..., min_length=1, max_length=255)
    description: str = Field(default="", max_length=1000)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Learn FastAPI",
                "description": "Complete the FastAPI tutorial"
            }
        }


class TaskUpdate(BaseModel):
    """Schema for updating a task"""
    name: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    completed: Optional[int] = Field(None)


class TaskResponse(BaseModel):
    """Schema for task response"""
    id: int
    name: str
    description: str
    completed: int
    created_at: datetime
    updated_at: datetime
    user_id: int

    class Config:
        from_attributes = True


# ============================================
# AUTH SCHEMAS
# ============================================

class Token(BaseModel):
    """Schema for JWT token response"""
    access_token: str
    token_type: str

    class Config:
        json_schema_extra = {
            "example": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                "token_type": "bearer"
            }
        }


class TokenData(BaseModel):
    """Schema for token data"""
    username: Optional[str] = None
