from typing import List, Optional

from pydantic import BaseModel, EmailStr


class CVInfoSchema(BaseModel):
    organization: List[str]
    major: List[str]
    gpa: List[str]
    name: List[str]
    skill: List[str]
    gender: List[str]
    job_title: List[str]
    profile_url: List[str]
    email: List[EmailStr]
    phone: List[str]