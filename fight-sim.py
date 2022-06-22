# simulating a fight between Thor and Loki
# '''
# thor attacks loki and deals 9 damage
# loki is down to 10 health
# loki attacks thor and deals 7 damage
# thor is down to 7 health
# thor attacks loki and deals 19 damage
# loki is down to -9 health
# loki has died and thor is victorious
# game over
# '''


import random
import math


class Warrior:
    def __init__(self, name="warrior", health=0, attk_max=0, block_max=0):
        self.name = name
        self.health = health
        self.attk_max = attk_max
        self.block_max = block_max

    def attack(self):
        attk_amt = self.attk_max * (random.random() + 0.5)
        return attk_amt

    def block(self):
        block_amt = self.block_max * (random.random() + 0.5)
        return block_amt


# utility class so there is no need to initialize anything
class Battle:
    def start_fight(self, warrior1, warrior2):
        while True:
            if self.get_attack_result(warrior1, warrior2) == "game over":
                print("game over")
                break
            if self.get_attack_result(warrior2, warrior1) == "game over":
                print("game over")
                break

    @staticmethod
    def get_attack_result(warrior_a, warrior_b):
        warrior_a_attk_amt = warrior_a.attack()
        warrior_b_block_amt = warrior_b.block()
        damage_to_warrior_b = math.ceil(warrior_a_attk_amt - warrior_b_block_amt)
        warrior_b.health = warrior_b.health - damage_to_warrior_b
        print("{} attacks {} and deals {} damage".format(warrior_a.name, warrior_b.name, damage_to_warrior_b))
        print("{} is down to {} health".format(warrior_b.name, warrior_b.health))
        if warrior_b.health <= 0:
            print("{} has died and {} is victorious".format(warrior_b.name, warrior_a.name))
            return "game over"
        else:
            return "fight again"


def main():
    thor = Warrior("thor", 50, 20, 10)
    loki = Warrior("loki", 50, 20, 10)
    battle = Battle()
    battle.start_fight(thor, loki)


main()
