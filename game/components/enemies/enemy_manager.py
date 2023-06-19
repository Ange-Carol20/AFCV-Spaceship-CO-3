from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_2 import Enemy2



class EnemyManager:
    def __init__(self):
        self.enemies: list[Enemy] = []
        self.enemy_spawned = False

    def update(self, game):
        if not self.enemies:
            if not self.enemy_spawned:
                self.enemies.append(Enemy())
                self.enemy_spawned = True
            else:
                self.enemies.append(Enemy2())
                self.enemy_spawned = False

        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def reset(self):
        self.enemies = []