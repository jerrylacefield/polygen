import math

def midpoint(a, b):
    mp = []
    mp.append((float(a[0]) + float(b[0])) / 2.00)
    mp.append((float(a[1]) + float(b[1])) / 2.00)
    
    return mp
    
def slope(a, b):
    if (b[0] - a[0] == 0):
        return "undefined"
    else:
        return (float(b[1])-float(a[1])) / (float(b[0])-float(a[0]))
    
def y_int(m, b):
    return ((-1) * m * b[0]) + b[1]
    
def collinear(m, b, c):
    return c[1] == m * c[0] + b
    
    
# 

def slope2(a, b):
    if (b.get_x() - a.get_x() == 0):
        return "undefined"
    else:
        return (b.get_y() - a.get_y()) / (b.get_x() - a.get_x())
        
def y_int2(m, b):
    return ((-1) * m * b.get_x()) + b.get_y()
    
def collinear2(m, b, x, y):
    return y == m * x + b