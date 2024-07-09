#!/usr/bin/env python3
'''coroutine will collect 10 random numbers using an async
comprehensing over async_generator, then return the 10 random numbers.'''
import asyncio
import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    '''Calls an async function and creates a list of float numbers
    returned from an async generator function'''
    random_numbers: typing.List[float]
    random_numbers = [i async for i in async_generator()]
    return random_numbers
