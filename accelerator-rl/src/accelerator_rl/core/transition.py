"""Transition data structures."""

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Transition:
    observation: Any
    action: Any
    reward: float
    next_observation: Any
    terminated: bool
    truncated: bool
    info: dict[str, Any]
