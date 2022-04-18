import aiohttp
import random
from typing import Union

from .stats import Stats

class Kawaii:
    def __init__(self, token):
        self.token = token
        self.url = "https://kawaii.red/api/"

    async def get(self, main: str, endpoint: str, f: Union[str, list]=None) -> str:
        if f is None:
            f = []
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}{main}/{endpoint}/token={self.token}&filter={f}/") as url:
                image = await url.json()
                return image["response"]

    async def text(self, text: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}txt/{text}/token={self.token}/") as url:
                image = await url.json()
                return image["response"]

    async def image(self, image: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}png/{image}/token={self.token}/") as url:
                image = await url.json()
                return image["response"]

    async def gif(self, gif: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}gif/{gif}/token={self.token}/") as url:
                image = await url.json()
                return image["response"]

    async def random(self, main: str=None) -> str:
        if main is None:
            main = "gif"
        endpoint = random.choice(await self.endpoints(main))
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}{main}/{endpoint}/token={self.token}/") as url:
                image = await url.json()
                return image["response"]

    async def endpoints(self, main: str=None) -> list:
        if main is None:
            main = "gif"
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}{main}/endpoints/token={self.token}/") as url:
                endpoints = await url.json()
                return endpoints["response"]

    async def stats(self) -> Stats:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}stats/endpoints/token={self.token}/") as url:
                endpoints = (await url.json())["response"]

            stats = {
                "endpoints": endpoints
            }

            for endpoint in endpoints:
                async with session.get(f"{self.url}stats/{endpoint}/token={self.token}/") as url:
                    stats[endpoint] = (await url.json())["response"]
            
            return Stats(**stats)
            