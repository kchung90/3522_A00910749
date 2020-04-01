"""
@author Kevin Chung

This module sends HTTP GET requests to retrieve Pokemon ability data
from the url and creates an Ability object.
"""
import aiohttp
import asyncio


class Ability:
    """
    Represents certain effects that pokemon can enable.
    """

    def __init__(self, name: str, id_value: int, generation: str,
                 effect: str, effect_short: str, pokemon: list):
        """
        Initializes an Ability object.
        :param name: name of the ability as a str
        :param id_value: id of the ability as an int
        :param generation: generation of the version introduced as a str
        :param effect: description of the effect as a str
        :param effect_short: short descripiton of the effect as a str
        :param pokemon: list of Pokemons
        """
        self.name = name
        self.id_value = id_value
        self.generation = generation
        self.effect = effect
        self.effect_short = effect_short
        self.pokemon = pokemon

    def __str__(self):
        """
        Returns the description of the Ability object
        :return: description as a str
        """
        return f"Pokemon Ability:\n" \
               f"Name: {self.name.title()}\n" \
               f"ID: {self.id_value}\n" \
               f"Generation: {self.generation}\n" \
               f"Effect: {self.effect}\n" \
               f"Effect Short: {self.effect_short}\n" \
               f"List of Pokemons: {self.pokemon}\n" \
               f"--------------------------------------------\n"


class Pokedex:
    """
    Represents a Pokedex that can send a single or multiple HTTP GET
    requests to query the Pokemon ability data from an url.
    """

    def __init__(self, url: str):
        """
        Initializes the Pokedex object
        :param url: url of an API as a str
        """
        self.url = url

    async def process_single_request(self, id_name):
        """
        Processes a single request to create an Ability object. Details
        of the Ability object are printed out at the end.
        :param id_name: a name/id of the ability as a str or an int
        """
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
        """
        Processes multiple requests to create Ability objects. Details
        of the Ability objects are printed out at the end.
        :param requests: list of a name/id of the ability
        """
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
        """
        Sends HTTP GET requests to retrieve the Pokemon ability data
        from an url.
        :param url: url of an API as a str
        :param session: aiohttp ClientSession
        :return: response as a JSON dictionary
        """
        response = await session.request(method="GET", url=url)
        json_response = await response.json()
        return json_response


def main():
    """
    Drives the program.
    """
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
