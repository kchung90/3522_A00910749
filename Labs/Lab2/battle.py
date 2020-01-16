"""
A simple automated battle system between two characters. Two characters
battle until one's health reaches zero.
"""

import random
from time import sleep


class Character:
    """
    Represent a character with a name, health, strength, critical hit
    chance, and dodge chance. Character objects can attack or defend.
    """
    def __init__(self, name, health, strength, critical_hit, dodge_chance):
        """
        Construct a character.
        :param name: name of the character as a String
        :param health: health of the character as a float
        :param strength: strength of the character as an int
        :param critical_hit: critical hit chance as a float
        :param dodge_chance: dodge chance as a float
        :precondition: critical_hit is a float between 0 and 0.1
        :precondition: dodge_chance is a float between 0 and 0.1
        """
        self.name = name
        self._health = health
        self.strength = strength
        self.critical_hit = critical_hit
        self.dodge_chance = dodge_chance

    @property
    def health(self):
        """
        Return health of the character.
        :return: health of the character as a String
        """
        if self._health > 0:
            return self._health
        return 0

    @property
    def is_alive(self):
        """
        Return boolean whether the character is alive or not.
        :return: True if the character is alive
        """
        if self._health > 0:
            return True
        return False

    def attack(self):
        """
        Attack the other character by dealing damage.
        :return: damage as an int
        """
        random_critical_hit_chance = random.random()
        damage = self.strength

        if random_critical_hit_chance < self.critical_hit:
            return damage * 2
        else:
            return damage

    def take_damage(self, damage):
        """
        Take damage from the other character if cannot dodge.
        :param damage: damage from the other character as an int
        :return: True if taken damage
        """
        random_dodge_chance = random.random()

        if random_dodge_chance < self.dodge_chance:
            self._health = self._health - damage
            return True
        else:
            return False


class BattleSimulator:
    """
    Represent a simulated battle between two characters. Facilitate
    attacks between two characters and declare a winner.
    """
    def __init__(self, character_1, character_2):
        """
        Construct the Battle Simulator by taking two Character objects.
        :param character_1: first character as a Character object
        :param character_2: second character as a Character object
        """
        self.character_1 = character_1
        self.character_2 = character_2

    def simulate(self):
        """
        Simulate the battle system.
        """
        while self.character_1.is_alive and self.character_2.is_alive:
            flip_coin = random.randint(0, 1)

            if flip_coin:
                attacker = self.character_1
                defender = self.character_2
            else:
                attacker = self.character_2
                defender = self.character_1

            damage = attacker.attack()

            if defender.take_damage(damage):
                if damage == 2 * attacker.strength:
                    print("- " * 25)
                    print(f"Critical Hit!\n{attacker.name} deals "
                          f"{damage}")
                    print(f"{defender.name} takes a hit! {defender.name} has "
                          f"{defender.health} remaining")
                else:
                    print("- " * 25)
                    print(f"{attacker.name} deals {damage}")
                    print(f"{defender.name} takes a hit! {defender.name} has "
                          f"{defender.health} remaining")
            else:
                if damage == 2 * attacker.strength:
                    print("- " * 25)
                    print(f"Critical Hit!\n{attacker.name} deals "
                          f"{damage}")
                    print(f"{defender.name} dodges the attack")
                else:
                    print("- " * 25)
                    print(f"{attacker.name} deals {attacker.attack()}")
                    print(f"{defender.name} dodges the attack")
            sleep(0.5)

        if self.character_1.health > 0:
            winner = f"{self.character_1.name}"
        else:
            winner = f"{self.character_2.name}"

        print("- " * 25)
        print("-" * 50)
        print(f"{winner} has won!!")
        print("\nFinal Stats:")
        print(f"Name: {self.character_1.name}, "
              f"Health: {self.character_1.health}, "
              f"Strength: {self.character_1.strength}, "
              f"Crit Chance: {self.character_1.critical_hit}, "
              f"Dodge Chance: {self.character_1.dodge_chance}")
        print(f"Name: {self.character_2.name}, "
              f"Health: {self.character_2.health}, "
              f"Strength: {self.character_2.strength}, "
              f"Crit Chance: {self.character_2.critical_hit}, "
              f"Dodge Chance: {self.character_2.dodge_chance}")
        print("-" * 50)


def main():
    """
    Create characters and the battle simulator. Drive the program.
    """
    character_1 = Character("Tiger", 50.0, 10, 0.3, 0.7)
    character_2 = Character("Lion", 60.0, 7, 0.3, 0.7)

    battle_simulator = BattleSimulator(character_1, character_2)
    battle_simulator.simulate()


if __name__ == '__main__':
    main()
