import aiohttp


async def load_matrix(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:
            if response.status >= 500:
                raise Exception("Server error")
            elif response.status >= 400:
                raise Exception("Client error")
            else:
                matrix = await response.text()
    return matrix
