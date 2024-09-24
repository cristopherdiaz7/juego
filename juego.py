import random
class Character:
    def __init__(self, name, class_type, health, strength, defense, level):
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

    def receive_item(self, item):
        self.items.append(item)
        if item['type'] == 'permanent':
            if item['attribute'] == 'strength':
                self.strength += item['value']
                print(f"{self.name} ha recibido {item['name']} y su fuerza ha aumentado a {self.strength}.")
            elif item['attribute'] == 'defense':
                self.defense += item['value']
                print(f"{self.name} ha recibido {item['name']} y su defensa ha aumentado a {self.defense}.")
        elif item['type'] == 'consumable':
            self.health += item['value']
            print(f"{self.name} ha usado {item['name']} y ha restaurado {item['value']} puntos de salud.")

class Enemy:
    def __init__(self, name, health, strength, defense):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense

    def attack(self, character):
        damage = max(0, random.randint(0, self.strength) - character.defense)
        character.health -= damage
        print(f"{self.name} ataca a {character.name} y causa {damage} de daño.")

    def is_alive(self):
            return self.health > 0

class Game:
    def __init__(self):
        self.heroes = self.generate_characters()
        self.items = self.generate_items()
        self.dungeons = self.generate_dungeons()

    def generate_characters(self):
        return [
            Character("The Warrior", "Warrior", 100, 15, 5, 1),
            Character("The mage", "Mage", 70, 10, 3, 1),
            Character("The Archer", "Archer", 80, 12, 4, 1)
        ]

    def generate_items(self):
        return [
            {'name': 'Ring of Strength', 'type': 'permanent', 'attribute': 'strength', 'value': 5},
            {'name': 'Cloak of Defense', 'type': 'permanent', 'atributte': 'defense', 'value': 3},
            {'name': 'Health Potion', 'type': 'consumable', 'value': 20},
            {'name': 'Strength Elixir', 'type': 'consumable', 'value': 5},
            {'name': 'Herb Bag', 'type': 'consumable', 'value': 10}
        ]