#!/usr/bin/env python3
'''Learning the Basic Async operation using async and random'''

import asyncio
import random
import typing

async def wait_random(max_delay: typing.Union[int, float] = 10):
    '''Basic usage of the async library to perform a simple async operation'''
    rand_sec = random.uniform(0, max_delay)
    await asyncio.sleep(rand_sec)
    return rand_sec
