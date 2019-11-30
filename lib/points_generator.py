import random
import formulas as geom

class Point:
    def __init__(self):
        self.p = []
    
    def set_point(self, plane):
        self.p.append(random.randint(plane['x_min'], plane['x_max']))
        self.p.append(random.randint(plane['y_min'], plane['y_max']))
        
    def reset_point(self, plane):
        self.p[0] = random.randint(plane['x_min'], plane['x_max'])
        self.p[1] = random.randint(plane['y_min'], plane['y_max'])
        
    def insert_point(self, plane, object_points, i):
        dupe = True
        collinear = True
        
        while dupe and collinear:
            if self.p in object_points:
                print("Point already inserted ... redefining point")
                self.reset_point(plane)
            elif i == 2:
                # print("testing collinearity")
                m = geom.slope(object_points[0], object_points[1])
                
                if m != "undefined":
                    b = geom.y_int(m , object_points[0])
                else:
                    b = "none"
                                
                if (m == "undefined" and self.p[0] == object_points[0][0]) or geom.collinear(m, b, self.p):
                    print("The new point is collinear")
                    print(self.p, " ---> ", object_points, m, b)
                    self.reset_point(plane)
                else:
                    object_points.append(self.p)
                    collinear = False
                    print("New point is noncollinear ... good to go")
                    print(m, b)
            else:
                object_points.append(self.p)
                dupe = False
        
                    
        #
        # while dupe:
        #     if self.p in points:
        #         self.p.reset_point(plane)
        #     else:
        #         points.append(self.p)
        #         dupe = False
    
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