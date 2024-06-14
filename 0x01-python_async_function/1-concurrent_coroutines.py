#!/usr/bin/env python3
"""
Module that defines an async routine to wait for multiple random delays.
"""

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay and return
    the list of delays in ascending order.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds for each wait_random.

    Returns:
        List[float]: The list of delays in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

    # Sort the list of delays without using sort()
    sorted_delays = []
    while delays:
        min_delay = min(delays)
        sorted_delays.append(min_delay)
        delays.remove(min_delay)

    return sorted_delays
