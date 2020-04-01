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
    pass


def main():
    pass


if __name__ == '__main__':
    main()
