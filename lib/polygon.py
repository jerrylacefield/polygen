import formulas as geom

class Edge:
    def __init__(self, e):
        self.e = e

class Triangle:
    def __init__(self):
        self.points = []
        self.edges = []
        self.midpoints = []
        self.medians = []
        self.centroid = []
        
    def create_edges(self):
        s = []
        test = self.points[1:]
        for i in range(len(self.points)):
            for j in range(len(test)):
                sub = [self.points[i], test[j]]
                self.edges.append(sub)
            if len(test) > 1:
                test.pop(0)
            else:
                break
        
    def find_midpoint(self):
        print(self.edges)
        for elem in self.edges:
            self.midpoints.append(geom.midpoint(elem[0], elem[1]))
        
    def print_points(self):
        print(self.points)