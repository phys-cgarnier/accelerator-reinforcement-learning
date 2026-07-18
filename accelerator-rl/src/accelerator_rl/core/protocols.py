"""Shared interfaces used across the framework."""

from typing import Any, Protocol


class SimulationBackend(Protocol):
    """Interface implemented by accelerator simulation backends."""

    def reset(self, *, seed: int | None = None) -> Any:
        """Reset the simulator and return its initial state."""

    def step(self, action: Any) -> Any:
        """Apply an action and return the updated simulation state."""


class RewardFunction(Protocol):
    """Interface for reward calculations."""

    def __call__(self, state: Any, action: Any, next_state: Any) -> float:
        """Compute one scalar reward."""
