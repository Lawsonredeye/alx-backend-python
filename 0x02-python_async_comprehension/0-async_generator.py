#!/usr/bin/env python3
'''Module which handles a coroutine generator function which returns an int'''

import asyncio
import typing


async def async_generator() -> typing.AsynGenerator[float, None]:

