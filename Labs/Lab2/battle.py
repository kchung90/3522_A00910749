import random
from time import sleep


class Character:
    def __init__(self, name, health, strength, critical_hit, dodge_chance):
        self.name = name
        self._health = health
        self.strength = strength
        self.critical_hit = critical_hit
        self.dodge_chance = dodge_chance

    @property
    def health(self):
        if self._health > 0:
            return self._health
        return 0

    @property
    def is_alive(self):
        if self._health > 0:
            return True
        return False

    def attack(self):
        random_critical_hit_chance = random.random()
        damage = self.strength

        if random_critical_hit_chance < self.critical_hit:
            return damage * 2
        else:
            return damage

    def take_damage(self, damage):
        random_dodge_chance = random.random()

        if random_dodge_chance < self.dodge_chance:
            self._health = self._health - damage
            return True
        else:
            return False


class BattleSimulator:
    def __init__(self, character_1, character_2):
        self.character_1 = character_1
        self.character_2 = character_2

    def simulate(self):
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

        if attacker.health > 0:
            winner = f"{attacker.name}"
        else:
            winner = f"{defender.name}"

        print("- " * 25)
        print("-" * 50)
        print(f"{winner} has won!!")
        print("\nFinal Stats:")
        print(f"Name: {self.character_1.name}, Health: "
              f"{self.character_1.health}, Strength: "
              f"{self.character_1.strength}, Crit Chance: "
              f"{self.character_1.critical_hit}, Dodge Chance: "
              f"{self.character_1.dodge_chance}")
        print(f"Name: {self.character_2.name}, Health: "
              f"{self.character_2.health}, Strength: "
              f"{self.character_2.strength}, Crit Chance: "
              f"{self.character_2.critical_hit}, Dodge Chance: "
              f"{self.character_2.dodge_chance}")
        print("-" * 50)


def main():
    character_1 = Character("A", 50.0, 10, 0.3, 0.7)
    character_2 = Character("B", 60.0, 7, 0.3, 0.7)

    battle_simulator = BattleSimulator(character_1, character_2)
    battle_simulator.simulate()


if __name__ == '__main__':
    main()






