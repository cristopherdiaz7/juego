import random
class character:
    def __init__(self, name, class_type, healt, strength, defense, level):
        self.name = name
        self.class_type = class_type
        self.health = healt
        self.strength = strength
        self.defense = defense
        self.level = level
        self.experience = 0
        self.items = []

    def attack(self, enemy):
        damage = max(0, random.randint(0, self.strength) - enemt.defense)
        enemy.healt -= damage
        print(f"{self.name} ataca a {enemy.name} y causa {damage} de daño.")

    def is_alive(self):
        return self.health > 0

    def level_up(self):
        self.level += 1
        self.health += 10
        self.strength += 2
        self.defense += 1
        self.experience = 0
        print(f"{self.name} ha subido al nivel {self.level}!")