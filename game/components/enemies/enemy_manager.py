from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_2 import Enemy2



class EnemyManager:
    def __init__(self):
        self.enemies: list[Enemy] = []

    def update(self, game):
        if not self.enemies:
            self.enemies.append(Enemy())
            self.enemies.append(Enemy2())


        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)