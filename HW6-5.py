class Stationary:
    def __init__(self, title = "Something that can drew"):
        self.title = title

    def draw(self):
        print(f" just start drawing! {self.title}")

class Pen(Stationary):
    def draw(self):
        print(f" just start drawing with pen! {self.title}")

stat = Stationary()
stat.draw()



