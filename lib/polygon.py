import random
import formulas as geom

class Edge:
    def __init__(self, e):
        self.e = e

class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        
    def __str__(self):
        return 'Point(' + str(self.x) + ', ' + str(self.y) + ')'
        
    def get_x(self):
        return self.x
        
    def get_y(self):
        return self.y
    
    def random_point(self, plane):    
        self.x = float(random.randint(plane['x_min'], plane['x_max']))
        self.y = float(random.randint(plane['y_min'], plane['y_max']))
        
    def set_point(self, x, y):
        self.x = float(x)
        self.y = float(y)
        
    def is_duplicate(self, object_points):
        for p in object_points:
            if self.x == p.x and self.y == p.y:
                return True
        
        return False
    
    def is_collinear(self, object_points):
       m = geom.slope2(object_points[0], object_points[1])
       
       if m != "undefined":
           b = geom.y_int2(m, object_points[0])
       else:
           b = "none"
           
       if (m == "undefined" and self.x == object_points[0].x) or geom.collinear2(m, b, self.x, self.y):
           return True
       else:
           return False
        
    def insert_point(self, plane, object_points, i):
        duplicate = True
        collinear = True
        
        while duplicate and collinear:
            print("testing " + self.__str__())
            if len(object_points) == 0:
                print("Adding first point " + self.__str__())
                # object_points.append(self)
                duplicate = False
            elif self.is_duplicate(object_points):
                print(self.__str__() + " already used ... redefining Point(x,y)")
                self.random_point(plane)
            elif i == 2:
                if self.is_collinear(object_points):
                    print(self.__str__() + " is collinear with " + object_points[0].__str__() + " and " + object_points[1].__str__())
                    print("Regenerating point ... ")
                    self.random_point(plane)
                else:
                    print(self.__str__() + " is non-collinear with " + object_points[0].__str__() + " and " + object_points[1].__str__())
                    # object_points.append(self)
                    collinear = False
            else:
                print("Adding new point " + self.__str__())
                # object_points.append(self)
                duplicate = False
            
            object_points.append(self)
            
            print("New Object Points")
            for p in object_points:
                print(p.x, p.y)
            
            # if test in object_points:
            #     print("Coorindates already used ... redefining x,y-coordinates")
            #     self.random_point(plane)
            # elif i == 2:
            #     print("testing collinearity")
            #     m = geom.slope2(object_points[0], object_points[1])
            #
            #     if m != "undefined":
            #         b = geom.y_int2(m , object_points[0])
            #     else:
            #         b = "none"
            #
            #     if (m == "undefined" and self.x == object_points[0].get_x()) or geom.collinear2(m, b, self.x, self.y):
            #         print("The new point is collinear")
            #         print(test, " ---> ", object_points, m, b)
            #         self.random_point(plane)
            #     else:
            #         object_points.append(test)
            #         collinear = False
            #         print("New point is noncollinear ... good to go")
            #         print(m, b)
            # else:
            #     object_points.append(test)
            #     duplicate = False
        
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

# Modules to test for certain characteristics as we build the polygons