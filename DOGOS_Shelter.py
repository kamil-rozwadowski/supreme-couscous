class Dogo(object):
    total=0
    def __init__(self,name='Rex',hunger = 3,bordnes=3):
        print("New dogo just born")
        self.__name=name
        self.hunger=hunger
        self.bordnes=bordnes
        Dogo.total+=1
    def __pass_time(self):
        self.hunger+=1
        self.bordnes+=1
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,new_name):
        if new_name == '':
            print("Dogo need name you cannot leave it blank")
        else:
            self.__name = new_name
            print('You just change Dogo name')
    @property
    def mood(self):
        if self.bordnes < 3:
            m='Happy'
        elif self.bordnes>=5:
            m='MAD'
        else:
            m='Bored'
        return m
    @property
    def starvation(self):
        if self.hunger < 3:
            h='Full'
        elif self.hunger>=5:
            h='SO HUNGRY'
        else:
            h='Hungry'
        return h
    @staticmethod
    def status():
        print('We have ',Dogo.total,' Dogos')
    def talk(self):
        print('\n Hello infidel my name is', self.__name,'and I am ',self.starvation,'and',self.mood)
        self.__pass_time()
    def eat(self):
        self.hunger=self.hunger-3
        self.__pass_time()
        if self.hunger<0:
            self.hunger=0
    def play(self):
        self.bordnes=self.bordnes-3
        self.__pass_time()
        if self.bordnes<0:
            self.bordnes=0

def main():
    Dog_Name = input('How you wanna named your Dogo ? \n')
    if Dog_Name == '':
        print('If you will not name him i will do it...\n His name is Rex')
        dog=Dogo()
    else:
        dog = Dogo(Dog_Name)
    chosse= None
    while 1==1:
        chosse=input('''\nHello in the DOGOS Sheleter tell me what you wanna do ?
        0 - close game.
        1 - Play with the Dogo
        2 - Feed your Dogo
        3 - Talk with your Dogo
        ''')
        if chosse == '1':
            dog.play()
        elif chosse == '2':
            dog.eat()
        elif chosse == '3':
            dog.talk()
        elif chosse == '0':
            break
    input('Press enter to end program')

main()



