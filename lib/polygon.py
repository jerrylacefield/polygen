class Triangle:
    def __init__(self):
        self.A = []
        self.B = []
        self.C = []
        
    def set_points(self, points):
        self.A = points[0]
        self.B = points[1]
        self.C = points[2]
        
    def print_points(self):
        print(self.A)
        
class Quadrilateral:
    def __init__(self, A, B, C, D):
        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0