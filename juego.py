import random
class Character:
    def __init__(self, name, class_type, health, strength, defense, level):
        self.name = name
        self.class_type = class_type
        self.health = health
        self.strength = strength
        self.defense = defense
        self.level = level
        self.experience = 0
        self.items = []

    def attack(self, enemy):
        damage = max(0, random.randint(0, self.strength) - enemy.defense)
        enemy.health -= damage
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
            {'name': 'Cloak of Defense', 'type': 'permanent', 'attribute': 'defense', 'value': 3},
            {'name': 'Health Potion', 'type': 'consumable', 'value': 20},
            {'name': 'Strength Elixir', 'type': 'consumable', 'value': 5},
            {'name': 'Herb Bag', 'type': 'consumable', 'value': 10}
        ]

    def generate_enemies(self):
        enemy_names = ["El Bandido", "El Rival", "El Fantasma", "El Mercenario", "La Bestia"]
        name = random.choice(enemy_names)
        health = random.randint(50, 100)
        strength = random.randint(5, 15)
        defense = random.randint(0, 5)
        return Enemy(name, health, strength, defense)

    def generate_dungeons(self):
        return [
            {"name": "Mazmorras de la Oscuridad", "enemies": [self.generate_enemies() for _ in range(2)],
             "boss": Enemy("Ladron Espectral", 80, 12, 5)},
            {"name": "Cueva de la Bestia", "enemies": [self.generate_enemies() for _ in range(3)],
             "boss": Enemy("Bestia Monstruosa", 100, 15, 8)},
            {"name": "Torre del Sabio", "enemies": [self.generate_enemies() for _ in range(2)],
             "boss": Enemy("El Gran Rival Oscuro", 90, 14, 6)}
        ]

    def combat(self, dungeons):
        for dungeon in dungeons:
            print(f"\nEntrando a {dungeon['name']}")
            for enemy in dungeon['enemies']:
                print(f"\n¡Un {enemy.name} aparece!")
                while enemy.is_alive() and any(hero.is_alive() for hero in self.heroes):
                    for i, hero in enumerate(self.heroes):
                        if hero.is_alive():
                            print(f"{i + 1}. {hero.name} (salud: {hero.health})")

                    selection = int(input("Selecciona un héroe para atacar (1-3): ")) - 1
                    if selection < 0 or selection >= len(self.heroes) or not self.heroes[selection].is_alive():
                        print("Seleccion inválida. Intenta de nuevo.")
                        continue  # Regresar al inicio del bucle para permitir otra selección

                    print(f"{self.heroes[selection].name} ha decidido atacar a {enemy.name}.")
                    self.heroes[selection].attack(enemy)
                    if enemy.is_alive():
                        enemy.attack(self.heroes[selection])
                    if not self.heroes[selection].is_alive():
                        print(f"¡{self.heroes[selection].name} ha sido derrotado por {enemy.name}!")

                if not enemy.is_alive():
                    print(f"¡{enemy.name} ha sido derrotado!")
                    item_obtained = random.choice(self.items)
                    self.heroes[selection].receive_item(item_obtained)
                    experience_gained = random.randint(20, 50)
                    self.heroes[selection].experience += experience_gained
                    print(f"{self.heroes[selection].name} ha ganado {experience_gained} puntos de experiencia.")
                    if self.heroes[selection].experience >= 50:
                        self.heroes[selection].level_up()

            boss = dungeon['boss']
            print(f"\n¡ jefe aparece: {boss.name}!")
            while boss.is_alive() and any(hero.is_alive() for hero in self.heroes):
                for i, hero in enumerate(self.heroes):
                    if hero.is_alive():
                        print(f"{i + 1}. {hero.name} (salud: {hero.health})")

                selection = int(input("Selecciona un héroe para atacar (1-3): ")) - 1
                if selection < 0 or selection >= len(self.heroes) or not self.heroes[selection].is_alive():
                    print("Seleccion inválida. Intenta de nuevo.")
                    continue

                print(f"{self.heroes[selection].name} ha decidido atacar a {boss.name}.")
                self.heroes[selection].attack(boss)

            if not boss.is_alive():
                print(f"¡{boss.name} ha sido derrotado!")

        print("¡Has completado todas las mazmorras!")

if __name__ == "__main__":
    game = Game()
    game.combat(game.dungeons)
