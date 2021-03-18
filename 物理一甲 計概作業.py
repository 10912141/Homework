import random
class chicken():
    def __init__(self,Sleepy=0,Hungry=0,Thirst=0,Boring=0,Hp=100):
        self.sleepy = Sleepy
        self.hungry = Hungry
        self.thirst = Thirst
        self.boring = Boring
        self.hp = Hp

    def _sleepy(self):
        self.sleepy = self.sleepy + 30

    def _hungry(self):   
        self.hungry = self.hungry + 30

    def _thirst(self):
        self.thirst = self.thirst + 30

    def _boring(self):
        self.boring = self.boring + 30

    def _hp(self):
        self.hp = self.hp - 30

    def _state(self):
        print('目前想睡值',self.sleepy)
        print('目前飢餓值',self.hungry)
        print('目前口渴值',self.thirst)
        print('目前無聊值',self.boring)
        print('目前血量',self.hp)
        
    def sleep(self):
        self.sleepy = self.sleepy - 15
    
    def feed(self):
        self.hungry = self.hungry - 15

    def drink(self):
        self.thirst = self.thirst - 15

    def play(self):
        self.boring = self.boring - 15

    def medicine(self):    
        self.hp = self.hp + 15
        
        
        


a = chicken()

while a.hp > 0:
    
    c=random.randint(1,5)
   
    if c==1:
        print('小雞想睡覺,想睡值+30:')
        a._sleepy()
    elif c==2:
        print('小雞肚子餓,飢餓值+30:')
        a._hungry()
    elif c==3:
        print('小雞口渴了,口渴值+30:')
        a._thirst()
    elif c==4:
        print('小雞好無聊,無聊值+30:')
        a._boring()
    elif c==5:
        print('小雞受傷了,血量-30:')
        a._hp()
    

    a._state()



    if a.sleepy > 80:

        a.hp-=20

    elif a.hungry > 80:    
        
        a.hp-=20

    elif a.thirst > 80:    
        
        a.hp-=20

    elif a.boring > 80:    
        
        a.hp-=20


    x=int(input('幫助小雞(請輸入) 1.sleep 2.feed 3.drink 4.play 5.medicine'))

    if x == 1:
        a.sleep()

    elif x == 2:
        a.feed()

    elif x == 3:
        a.drink()    

    elif x == 4:
        a.play()

    elif x == 5:
        a.medicine()
    else:
        print("error")

print('Game Over')


main()











        




















