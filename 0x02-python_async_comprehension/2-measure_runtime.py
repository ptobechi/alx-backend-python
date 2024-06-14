#!/usr/bin/env python3
"""
Module that defines a coroutine to measure the runtime of async_comprehension.
"""

import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in in
    parallel using asyncio.gather,
    measures the total runtime, and returns it.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = asyncio.get_event_loop().time()  # Get the current event loop time
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = asyncio.get_event_loop().time()  # Get the current event loop time after execution
    total_runtime = end_time - start_time
    return total_runtime
