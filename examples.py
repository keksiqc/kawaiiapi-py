import asyncio
from kawaiiapi import Kawaii

api = Kawaii("anonymous")

loop = asyncio.get_event_loop()

print(loop.run_until_complete(api.endpoints("gif")))

print(loop.run_until_complete(api.random("gif")))

print(loop.run_until_complete(api.get("gif", "kiss")))

print(loop.run_until_complete(api.gif("kiss")))

print(loop.run_until_complete(api.stats()).all)