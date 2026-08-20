class Geom:
    name = 'Geom'


    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x1 = x2
        self.y1 = y2
        self.draw()


class Line(Geom):
    def draw(self):
        print("Малювання лінії")





class Rect(Geom):
    def draw(self):
        print("Малювання прямокутника")





#g = Geom()
l = Line()
r = Rect()
l.set_coords(1, 1, 2, 3,)
r.set_coords(2, 1, 3, 4)
#print(l.__dict__)
#print(r.__dict__)




