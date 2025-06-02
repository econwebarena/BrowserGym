"""
EconWebArena Task
"""
import logging
from typing import Tuple

from browsergym.core.task import AbstractBrowserTask
from datasets import load_dataset, Features, Value
from playwright.sync_api import Page

logger = logging.getLogger(__name__)

# Load datasets
features = Features({
    "id": Value("int32"),
    "website": Value("string"),
    "task": Value("string"),
    "task_url": Value("string"),
    "answer": Value("string"),
    "answer_key": Value("string"),
    "answer_url": Value("string"),
    "category": Value("string"),
    "seed": Value("bool"),
})
datasets = load_dataset(
    "EconWebArena/EconWebArena",
    features=features,
)

# Load tasks
tasks = {f"{row['id']}": row["task"] for row in datasets["test"]}
task_urls = {f"{row['id']}": row["task_url"] for row in datasets["test"]}
answers = {f"{row['id']}": row["answer"] for row in datasets["test"]}
answer_keys = {f"{row['id']}": row["answer_key"] for row in datasets["test"]}


class EconWebArenaTask(AbstractBrowserTask):
    """
    BrowserGym task definition for EconWebArena.
    """

    def __init__(self, seed: int, task_id: str) -> None:
        """
        Args:
            seed (int): Random seed for task initialization.
            task_id (str): Unique identifier for the task (for the BrowserGym environment).
        """
        super().__init__(seed)
        self.task_id = task_id
        self.task = tasks[task_id]
        self.task_url = task_urls[task_id]
        self.answer = answers[task_id]
        self.answer_key = answer_keys[task_id]
        self.goal = (
            f"{self.task} "
            f"The answer must come from a URL containing \"{self.answer_key}\"."
        )
        self.gold = self.answer

    def setup(self, page: Page) -> Tuple[str, dict]:
        """
        Set up everything needed to execute the task.

        Args:
            page: the active playwright page.

        Returns:
            goal: str, goal of the task.
            info: dict, custom information from the task.
        """
        logger.info(f"Navigating to the start URL: {self.task_url}")
        page.goto(self.task_url, timeout=30_000, wait_until="load")
        return self.goal, {}

    def validate(self, page: Page, chat_messages: list[dict]) -> Tuple[float, bool, str, dict]:
        """
        Validate the task was completed successfully

        Args:
            page: the active playwright page.
            chat_messages: the chat messages.

        Returns:
            reward: float, the reward obtained since last call to validate().
            done: boolean flag, indicates if the task has finished or not (be it success or fail).
            message: string, a new user message for the chat.
            info: dictionary, custom information from the task.

        """
        reward, done, message, info = 0.0, False, "", {}

        # Evaluate when the agent returns a response
        if chat_messages and chat_messages[-1]["role"] == "assistant":
            done = True
            prediction = chat_messages[-1]["message"]
            reward = (self.gold in prediction) and (self.answer_key in page.url)

        return reward, done, message, info
