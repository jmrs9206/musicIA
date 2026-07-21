from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseAgent(ABC):
    def __init__(self, name: str, role_description: str):
        self.name = name
        self.role_description = role_description

    def log(self, message: str) -> None:
        print(f"[{self.name}] {message}")

    @abstractmethod
    def run(self, *args: Any, **kwargs: Any) -> Any:
        pass
