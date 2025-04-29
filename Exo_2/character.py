import random

class Character:
    def __init__(self, name: str):
        self.name = name
        self.life = 100.0  # Vie de base
        self.attack = 20.0  # Attaque de base
        self.defense = 0.1  # Réduction de dégâts (10%)

    def take_damage(self, damage: float):
        """Applique les dégâts après réduction de défense."""
        actual_damage = damage * (1 - self.defense)
        self.life -= actual_damage
        if self.life < 0:
            self.life = 0

    def attack_enemy(self, enemy: 'Character'):
        """Attaque un autre personnage."""
        enemy.take_damage(self.attack)

    def is_dead(self):
        """Vérifie si le personnage est mort."""
        return self.life <= 0

    def __repr__(self):
        return f"{self.name} <{self.life:.1f}>"

class Warrior(Character):
    def __init__(self, name: str):
        super().__init__(name)
        self.life *= 1.5  # Vie augmentée
        self.defense *= 1.2  # Défense augmentée
        self.weapon_attack = 5.0  # Attaque de base de l'arme

    def attack_enemy(self, enemy: 'Character'):
        """L'attaque inclut les dégâts de l'arme."""
        total_attack = self.attack + self.weapon_attack
        if self.life < 30:  # Rage si vie inférieure à 30
            total_attack *= 1.2  # Augmente les dégâts de 20%
        enemy.take_damage(total_attack)

class Magician(Character):
    def __init__(self, name: str):
        super().__init__(name)
        self.life *= 0.8  # Vie réduite de 20%
        self.attack *= 2  # Attaque doublée

    def take_damage(self, damage: float):
        """Si le bouclier magique est activé, les dégâts sont annulés."""
        if random.random() < 0.33:  # 33% de chance d'activer le bouclier
            print(f"{self.name} bloque les dégâts avec son bouclier magique !")
        else:
            super().take_damage(damage)

class Combat:
    def __init__(self, characters: list):
        self.characters = characters

    def turn(self):
        """Mélange l'ordre des combattants et fait attaquer tous les personnages vivants."""
        random.shuffle(self.characters)
        for character in self.characters:
            if not character.is_dead():
                for target in self.characters:
                    if target != character and not target.is_dead():
                        character.attack_enemy(target)

    def is_game_over(self):
        """Vérifie si un seul personnage est encore vivant."""
        return sum(1 for character in self.characters if not character.is_dead()) <= 1

    def display_status(self):
        """Affiche l'état actuel des personnages."""
        for character in self.characters:
            print(character)

