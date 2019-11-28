import formulas as geom

class Edge:
    def __init__(self, e):
        self.e = e

class Triangle:
    def __init__(self, t):
        self.t = t
        self.edges = []
        self.midpoints = []
        self.medians = []
        self.centroid = []
        
    def create_edges(self):
        s = []
        test = self.t[1:]
        for i in range(len(self.t)):
            for j in range(len(test)):
                sub = [self.t[i], test[j]]
                self.edges.append(sub)
            if len(test) > 1:
                test.pop(0)
            else:
                break
        # print(self.edges)
        
    def find_midpoint(self):
        print(self.edges)
        for elem in self.edges:
            self.midpoints.append(geom.midpoint(elem[0], elem[1]))
        
    def print_points(self):
        print(self.t)