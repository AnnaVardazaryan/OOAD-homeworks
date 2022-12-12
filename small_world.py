import time

class Frog:
    def __init__(self):
        self.hungry = True

    def day_of_frog(self):
        time.sleep(2)
        print("Frog:is breathing, moving")
        if self.hungry:
            time.sleep(2)
            print("Frog is eating grass")
        self.hungry = False

    def night_of_frog(self):
        time.sleep(2)
        print("Frog:is sleeping")
        self.hungry = True

class Tree:
    def __init__(self, frog: Frog):
        self.oxygen = False
        self.frog = frog

    def day_of_tree(self):
        self.oxygen = True
        time.sleep(2)
        print("Tree:is creating oxygen")
        self.frog.day_of_frog()

    def night_of_tree(self):
        self.oxygen = False
        time.sleep(2)
        print("Tree:is not creating oxygen")
        self.frog.night_of_frog()

class Sun:
    def __init__(self, light, tree: Tree):
        self.light = light
        self.tree = tree

    def day_in_world(self):
        while True:
            time.sleep(2)
            if self.light:
                print("Sun:is shining")
                self.tree.day_of_tree()
                self.light = False
            if not self.light:
                print("Sun:is not shining")
                self.tree.night_of_tree()
                self.light = True


frog = Frog()
tree = Tree(frog)
sun = Sun(True, tree)
sun.day_in_world()