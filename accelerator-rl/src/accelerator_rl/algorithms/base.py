"""Base algorithm interface."""

from abc import ABC, abstractmethod
from typing import Any


class Algorithm(ABC):
    @abstractmethod
    def update(self, batch: Any) -> dict[str, float]:
        """Update trainable parameters from a rollout batch."""
