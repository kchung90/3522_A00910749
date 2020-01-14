from random import random

class Character:
    def __init__(self, name, health, strength, dodge_chance, critical_hit):
        self.name = name
        self.health = health
        self.strength = strength
        self.dodge_chance = dodge_chance
        self.critical_hit = critical_hit

    def read_health(self):
        if self.health > 0:
            return self.health
        return 0

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def attack(self):
        critical_hit_chance = 0.3
        random_number = random()
        damage = self.strength

        if random_number < critical_hit_chance:
            return damage * 2
        return damage

    def take_damage(self, damage):
        dodge_chance = 0.3
        random_number = random()

        if random_number < dodge_chance:
            return True
        else:
            self.health -= damage
            return False


class BattleSimulator:
    pass


