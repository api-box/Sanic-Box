from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Union

from box.entities.article import UserAccount


@dataclass(frozen=True)
class Article:
    id: str
    author: Optional[UserAccount]
    description: str
    like_count: int
    file_path: Optional[str]


@dataclass(frozen=True)
class Post(Article):
    title: str
    summary: Optional[str]
    shared_count: int


@dataclass(frozen=True)
class Comment(Article):
    root: Union[Post, Comment]
