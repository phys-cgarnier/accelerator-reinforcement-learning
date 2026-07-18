"""Trajectory data structures."""

from dataclasses import dataclass, field

from accelerator_rl.core.transition import Transition


@dataclass(slots=True)
class Trajectory:
    transitions: list[Transition] = field(default_factory=list)
