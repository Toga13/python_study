class Character:
    def __init__(self, name, hp, offensive_power, difensive_power, speed):
        self.name = name                          #名前
        self.hp = hp                              #体力
        self.offensive_power = offensive_power    #攻撃力
        self.difensive_power = difensive_power    #防御力
        self.speed = speed                        #攻撃スピード

    def display(self):
        print (f"{self.name}のスペック")
        print ("体力:"f"{self.hp}")
        print ("攻撃力："f"{self.offensive_power}")
        print ("防御力："f"{self.difensive_power}")
        print ("スピード："f"{self.speed}")

class Hero(Character):
    def __init__(self, name, hp, offensive_power, difensive_power, speed):
        super (Hero, self).__init__(name, hp, offensive_power, difensive_power, speed)

    def attack(self, enemy):
        enemy_hp = enemy.hp
        hero_hp = hero.hp                       #勇者のアタックメソッド
        if hero.speed > enemy.speed:
            while True:
                print (hero.name,"の攻撃")
                enemy_hp = enemy_hp - (hero.offensive_power - enemy.difensive_power)
                if enemy_hp <= 0:
                    enemy_hp = 0
                    winner = hero.name
                print (enemy.name,"のHP:",enemy_hp)
                print (enemy.name,"の攻撃")
                hero_hp = hero_hp - (enemy.offensive_power - hero.difensive_power)
                if  hero_hp <= 0:
                    hero_hp = 0
                    winner = enemy.name
                print (hero.name,"のHP：",hero_hp)
                if enemy_hp <= 0 or hero_hp <= 0 :
                    break
        else:
            while hero.hp > 0 or enemy.hp > 0 :
                print (enemy.name,"の攻撃")
                hero_hp = hero_hp - (enemy.offensive_power - hero.difensive_power)        
                if  hero_hp < 0:
                    hero_hp = 0
                    winner = enemy.name
                print (hero.name,"のHP：",hero_hp)
                print (hero.name,"の攻撃")
                enemy_hp = enemy_hp - (hero.offensive_power - enemy.difensive_power)
                if enemy_hp < 0:
                    enemy_hp = 0
                    winner = hero.name
                print (enemy.name,"のHP：",enemy_hp)
                if enemy_hp <= 0 or hero_hp <= 0 :
                    break
        print (winner,"の勝利！！")

class Enemy(Character):
    def __init__(self, name, hp, offensive_power, difensive_power, speed):
        super (Enemy, self).__init__(name, hp, offensive_power, difensive_power, speed)

hero_name = input ('Heroの名前')
hero_hp = input ('HeroのHPを入力してください')


hero = Hero(hero_name), hero_hp, 50, 30, 50)
enemy = Enemy("バイキンマン", 120, 40, 40, 40)
hero.display()
enemy.display()
hero.attack(enemy)
