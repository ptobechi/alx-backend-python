#!/usr/bin/env python3
"""
Module that defines a function to return an asyncio.Task for wait_random.
"""

import asyncio
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: The asyncio.Task object for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
