from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class Credential:
    access_token: str
    refresh_token: str


@dataclass(frozen=True)
class UserAccount:
    email: str
    password: str
    age: int
    image_path: Optional[str]
    birthday: Optional[datetime]
    name: str
    bio: Optional[str]
    credential: Optional[Credential]
