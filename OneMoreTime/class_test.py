class Pet(object):
    def __init__(self, name):
        self.name = name
        print(self.name)

    def do(self):
        pass


class Cat(Pet):
    def go(self):
        print("New GO instance")


print(Pet("My object Name").do())
