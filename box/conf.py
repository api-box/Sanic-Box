import os
from dataclasses import dataclass

ENV = os.environ


@dataclass(frozen=True)
class Config:
    HOST: str = ENV.get('HOST', 'localhost')
    PORT: int = int(ENV.get('PORT', 9090))
    DEBUG: bool = 'true' == ENV.get('DEBUG', 'true').lower()
