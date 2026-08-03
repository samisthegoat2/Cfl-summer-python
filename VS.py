import random


class FFighter:
    def __init__(self,name,sword,damage,health):
        self.name = name
        self.sword  = sword
        self.damage = damage
        self.health = health

    def attack(self,Opponent):
        damage = random.randint(1, self.damage)
        Opponent.health -= damage
        print(f"{self.name} attacks {Opponent.name} and deals {damage} damage")


    def is_hurt(self):
        return self.health <= 0

class plumber(FFighter):
    def __init__(self, name, damage, health,plumber_hammer):
        super().__init__(name,damage, health)
        self.hammer = plumber_hammer

    def attack(self, Opponent):
      damage = random.randint(self.hammer, self.damage)
      Opponent.health -= damage
      print(F"{self.name} hit him with his, hammer and deals {damage} damage to {Opponent.name}.")

def main():
    fighter1 = FFighter("Mario", "sword", 10,100)
    fighter2 = plumber("luigi", 8, 100, 15)

    while FFighter. is_hurt() and plumber.is_hurt():
        fighter1.attack(fighter2)
        if not fighter2.is_hurt():
            break
        fighter2.attack(fighter1)


        if fighter1.is_hurt():
            print(f"{fighter1.name} has been defeated!")
            break
main()
        



                  
                                              

              

              
                
           













