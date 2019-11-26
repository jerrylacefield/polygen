import random

class Point:
    def __init__(self):
        self.p = []
    
    def set_point(self, plane):
        self.p.append(random.randint(plane['x_min'], plane['x_max']))
        self.p.append(random.randint(plane['y_min'], plane['y_max']))
        
    def reset_point(self, plane):
        self.p[0] = random.randint(plane['x_min'], plane['x_max'])
        self.p[1] = random.randint(plane['y_min'], plane['y_max'])
        
    def insert_point(self, plane, points, p):
        dupe = True
        while dupe:
            if self.p in points:
                self.p.reset_point(plane)           
                # self.p[0] = random.randint(plane['x_min'], plane['x_max'])
                # self.p[1] = random.randint(plane['y_min'], plane['y_max'])
            else:
                points.append(self.p)
                dupe = False
    
    def print_point(self, name):
        print(name + "(" + str(self.p[0]) + "," + str(self.p[1]) + ")")
    
    def get_point(self):
        return self.p
    
    def get_x(self):
        return self.p[0]
        
    def get_y(self):
        return self.p[1]

def minimum_range(max):
    return -2 * max + max

def coordinate_plane(plane):
    xMax = int(raw_input("What is the max x-value range? "))
    yMax = int(raw_input("What is the max y-value range? "))

    plane['x_max'] = xMax
    plane['y_max'] = yMax
    plane['x_min'] = minimum_range(xMax)
    plane['y_min'] = minimum_range(yMax)
    
def generate_point(plane, point):
    x = random.randint(plane['x_min'], plane['x_max'])
    y = random.randint(plane['y_min'], plane['y_min'])
    
    point['x'] = x
    point['y'] = y

def insert_point(plane, points, p):  
    dupe = True
    while dupe:
        if p.get_point() in points:
            p.reset_point(plane)
        else:
            points.append(p.get_point())
            dupe = False