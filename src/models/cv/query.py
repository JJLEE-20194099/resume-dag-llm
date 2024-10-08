from typing import List, Optional

from pydantic import BaseModel, EmailStr


class CVQuerySchema(BaseModel):
    organization: Optional[List[str]] = None
    major: Optional[List[str]] = None
    gpa: Optional[List[str]] = None
    name: Optional[List[str]] = None
    skill: Optional[List[str]] = None
    gender: Optional[List[str]] = None
    job_title: Optional[List[str]] = None
    profile_url: Optional[List[str]] = None
    email: Optional[List[EmailStr]] = None
    phone: Optional[List[str]] = None
    batch_id: Optional[str] = None
    education: Optional[List[str]] = None

    class Config:
        require_by_default = False