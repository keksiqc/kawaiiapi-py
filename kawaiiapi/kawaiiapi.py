import aiohttp
import random
from typing import Union

from .stats import Stats

class Kawaii:
    def __init__(self, token: str = ""):
        self.token = token
        self.url = "https://kawaii.red/api/"

    async def get(self, type: str, endpoint: str, f: Union[str, list] = []) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}{type}/{endpoint}/token={self.token}&filter={f}/") as url:
                image = await url.json()
                return image.get("response")

    async def text(self, text: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}txt/{text}/token={self.token}/") as url:
                image = await url.json()
                return image.get("response")

    async def image(self, image: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}png/{image}/token={self.token}/") as url:
                image = await url.json()
                return image.get("response")

    async def gif(self, gif: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}gif/{gif}/token={self.token}/") as url:
                image = await url.json()
                return image.get("response")

    async def random(self, type: str = "gif") -> str:
        endpoint = random.choice(await self.endpoints(type))
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}{type}/{endpoint}/token={self.token}/") as url:
                image = await url.json()
                return image.get("response")

    async def endpoints(self, type: str="gif") -> list:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}{type}/endpoints/token={self.token}/") as url:
                endpoints = await url.json()
                return endpoints.get("response")

    async def stats(self) -> Stats:
        if self.token == "anonymous":
            raise Exception("You need to set a token to use this function")

        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}stats/endpoints/token={self.token}/") as url:
                endpoints = (await url.json()).get("response")

            stats = {
                "endpoints": endpoints
            }

            for endpoint in endpoints:
                async with session.get(f"{self.url}stats/{endpoint}/token={self.token}/") as url:
                    stats[endpoint] = (await url.json()).get("response")
            
            return Stats(**stats)
            