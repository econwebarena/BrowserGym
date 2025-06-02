__version__ = "0.14.0"

from playwright.sync_api import sync_playwright, Playwright
from threading import Lock
import atexit

# we use a global playwright instance
_PLAYWRIGHT = None
_PLAYWRIGHT_LOCK = Lock()


def _set_global_playwright(pw: Playwright):
    global _PLAYWRIGHT
    _PLAYWRIGHT = pw


def _get_global_playwright():
    global _PLAYWRIGHT
    with _PLAYWRIGHT_LOCK:
        if _PLAYWRIGHT is None:
            _PLAYWRIGHT = sync_playwright().start()
            atexit.register(lambda: _PLAYWRIGHT.stop())
    return _PLAYWRIGHT


# register the open-ended task
from .registration import register_task
from .task import OpenEndedTask

register_task(OpenEndedTask.get_task_id(), OpenEndedTask)
