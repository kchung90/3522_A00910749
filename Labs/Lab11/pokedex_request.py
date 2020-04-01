import aiohttp
import asyncio


class Ability:

    def __init__(self, name: str, id_value: int, generation: str,
                 effect: str, effect_short: str, pokemon: list):
        self.name = name
        self.id_value = id_value
        self.generation = generation
        self.effect = effect
        self.effect_short = effect_short
        self.pokemon = pokemon


class PokedexRequest:

    def __init__(self, url: str):
        self.url = url

    async def process_requests(self, requests: list):
        async with aiohttp.ClientSession() as session:
            list_urls = [self.url.format(req_id) for req_id in requests]
            coroutines = [self.get_ability_data(my_url, session)
                          for my_url in list_urls]
            responses = await asyncio.gather(*coroutines)
            for response in responses:
                print(response)

    @classmethod
    async def get_ability_data(cls, url: str, session: aiohttp.ClientSession):
        response = await session.request(method="GET", url=url)
        json_response = await response.json()
        return json_response


def main():
    pass


if __name__ == '__main__':
    main()
