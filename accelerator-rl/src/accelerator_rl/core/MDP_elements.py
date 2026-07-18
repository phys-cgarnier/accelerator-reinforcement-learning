
from dataclasses import dataclass, field
from typing import Any

@dataclass(slots=True)
class State:
    pass

@dataclass(slots=True)
class Action:
    pass

@dataclass(slots=True)
class Observable:
    pass

@dataclass(slots=True)
class Reward:
    pass

@dataclass(slots=True)
class Transition:
    observation: Any
    action: Any
    reward: float
    next_observation: Any
    terminated: bool
    truncated: bool
    info: dict[str, Any]

@dataclass(slots=True)
class Trajectory:
    transitions: list[Transition] = field(default_factory=list)