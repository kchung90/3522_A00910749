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

    def __str__(self):
        return f"Pokemon Ability:\n" \
               f"Name: {self.name.title()}\n" \
               f"ID: {self.id_value}\n" \
               f"Generation: {self.generation}\n" \
               f"Effect: {self.effect}\n" \
               f"Effect Short: {self.effect_short}\n" \
               f"List of Pokemons: {self.pokemon}\n" \
               f"--------------------------------------------\n"


class Pokedex:

    def __init__(self, url: str):
        self.url = url

    async def process_single_request(self, id_name):
        url = self.url.format(id_name)
        async with aiohttp.ClientSession() as session:
            response = await self.get_ability_data(url, session)
            for entry in response["effect_entries"]:
                ability_effect = entry["effect"].replace("\n", " ")
                ability_short_effect = entry["short_effect"]
            ability_pokemon_list = [pokemon["pokemon"]["name"] for
                                    pokemon in response["pokemon"]]
            print(Ability(response["name"], response["id"],
                          response["generation"]["name"], ability_effect,
                          ability_short_effect, ability_pokemon_list))

    async def process_requests(self, requests: list):
        async with aiohttp.ClientSession() as session:
            list_urls = [self.url.format(id_name) for id_name in requests]
            coroutines = [self.get_ability_data(my_url, session)
                          for my_url in list_urls]
            responses = await asyncio.gather(*coroutines)
            for response in responses:
                ability_name = response["name"]
                ability_id = response["id"]
                ability_gen = response["generation"]["name"]
                for entry in response["effect_entries"]:
                    ability_effect = entry["effect"].replace("\n", " ")
                    ability_short_effect = entry["short_effect"]
                ability_pokemon_list = [pokemon["pokemon"]["name"] for
                                        pokemon in response["pokemon"]]
                print(Ability(ability_name, ability_id, ability_gen,
                              ability_effect, ability_short_effect,
                              ability_pokemon_list))

    @classmethod
    async def get_ability_data(cls, url: str, session: aiohttp.ClientSession):
        response = await session.request(method="GET", url=url)
        json_response = await response.json()
        return json_response


def main():
    pokedex = Pokedex("https://pokeapi.co/api/v2/ability/{}")

    # -----------------------------
    # Single Request
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(pokedex.process_single_request(1))

    # -----------------------------
    # Multiple Requests
    requests = [1, 2, 3]
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(pokedex.process_requests(requests))


if __name__ == '__main__':
    main()
