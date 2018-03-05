#!/usr/bin/env python

"""
Ultra simple async
"""

import asyncio

async def say_lots(num):
    for i in range(num):
        print('This was run by the loop:')
        await asyncio.sleep(0.2)

# getting an event loop
loop = asyncio.get_event_loop()
# run it:
loop.run_until_complete(say_lots(5))
print("done with loop")
loop.close()
