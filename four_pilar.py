
class Bird:
    def fly(self):
        return "Bird is flying"

class Airplane:
    def fly(self):
        return "Airplane is flying"

def let_it_fly(flyer):
    print(flyer.fly())

bird = Bird()
airplane = Airplane()

let_it_fly(bird)
let_it_fly(airplane)