class Player:
    def __init__(self):
        self.gold_coins = 0
        self.health_points = 10
        self.lives = 5

    def __str__(self):
        return "{}, {} and {}".format(self.gold_coins, self.health_points, self.lives)

    def level_up(self):
        self.lives += 1

    def collect_treasure(self):
        self.gold_coins += 1
        if self.gold_coins % 10 == 0:
            self.level_up()

    def do_battle(self, damage):
        self.health_points -= damage
        if self.health_points < 1:
            self.lives -= 1 
            self.health_points = 10
        if self.lives < 1:
            self.restart()

    def restart(self):
        self.gold_coins = 0
        self.health_points = 10
        self.lives = 5

player_one = Player()
print(player_one.__str__())
print(player_one.level_up())
print(player_one.__str__())
print(player_one.collect_treasure())
print(player_one.__str__())
print(player_one.do_battle(1))
print(player_one.__str__())
print(player_one.restart())
print(player_one.__str__())
