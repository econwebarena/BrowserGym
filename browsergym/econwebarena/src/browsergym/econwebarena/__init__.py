"""
EconWebArena Initialization
"""
from browsergym.core.registration import register_task

from . import task

ALL_AB_TASK_IDS = []

# Register the EconWebArena test set
for task_id in range(1, 361):
    gym_id = f"econwebarena.{task_id}"
    register_task(
        gym_id,
        task.EconWebArenaTask,
        task_kwargs={
            "task_id": f"{task_id}",
        },
        default_task_kwargs={},
    )
    ALL_AB_TASK_IDS.append(gym_id)
