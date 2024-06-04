class playercharacters:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def run(self):
        print('run')
        return 'done'
player1= playercharacters('Ali',34)
player2= playercharacters('hassan',32)
player3= playercharacters('khan',30)
player2.attack = 50

print(player1.run())
print(player2.attack)
print(player3.age)