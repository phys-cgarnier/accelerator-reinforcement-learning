# Accelerator RL

Skeleton repository for a reinforcement-learning framework built around accelerator physics simulations.

This repository intentionally contains structure and interfaces only. It does not include a concrete environment or training implementation.

## Architecture

- `algorithms/`: RL algorithms such as REINFORCE, PPO, and SAC
- `agents/`: Action-selection and agent composition
- `environments/`: Gymnasium-compatible accelerator environments
- `simulation/`: Simulation backends such as Cheetah
- `rewards/`: Reward definitions and composition
- `constraints/`: Physical and control constraints
- `rollouts/`: Trajectory collection and storage
- `models/`: Policy and value networks
- `training/`: Training, evaluation, and checkpoint orchestration
- `analysis/`: Physics sensitivity and trajectory analysis

## Installation

```bash
uv sync --all-extras
```

or

```bash
python -m pip install -e ".[dev]"
```

## Development

```bash
pytest
ruff check .
mypy src
```

## Intended dependency direction

```text
scripts
  ↓
training
  ↓
algorithms ← rollouts ← environments
                         ↓
                     simulation
                         ↓
               rewards + constraints
```

The algorithm layer should not depend on Cheetah. The simulation layer should not depend on any RL algorithm.
