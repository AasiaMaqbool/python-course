class Cat:
    def __init__(self):
        self._sound="meow"
    def speak(self):
        print("cat says:{}".format(self._sound))

c=Cat()
c.speak()
#when changes in prices
c.sound="bow.wow"
c.speak()
