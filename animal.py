class Animal:                        #Animalクラス定義
    def __init__(self):              #特殊関数
        self.leg_num = 4             #属性
        self.is_tail = True          #属性
    
    def run(self):                   #機能
         print ("走る")

    def bark(self):                  #機能
        print ("鳴く")

class Dog(Animal):                   #Dogクラス定義
    def __init__(self):              #特殊関数
        self.is_fauthfull = True     #属性

    def bark(self):                  #機能，オーバーライド（クラスの継承）
        print ("ワンワン")

class Cat(Animal):                   #Catクラス定義
    def __init__(self):
        pass

    def jump(self):                  #機能
        print ("ジャンプする")
    
    def bark(self):                  #機能，オーバーライド
        print ("ニャンニャン")

dog = Dog()
dog.bark()

cat = Cat()
cat.bark()
cat.jump()