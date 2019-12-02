import lib.points_generator as PO
import lib.polygon as polygon
import lib.graphics as g
# from lib.graphics import *

def define_points(n):
    for i in range(n):
        points_list.append(PO.Point())
        points_list[i].set_point(plane)
        points_list[i].insert_point(plane, object_points, i)

plane = {'x_max':0, 'y_max':0,'x_min':0,'y_min':0}

triangles = []
object_points = []
points_list = []

PO.coordinate_plane(plane)

# for i in range(3):
#     points_list.append(PG.Point())
#     points_list[i].set_point(plane)
#     points_list[i].insert_point(plane, points, points_list[i])

for i in range(1):
    triangles.append(polygon.Triangle())
    define_points(3)
    triangles[i].points = object_points[0:]
    del points_list[:]
    del object_points[:]
    # print(triangles[i].points)
    
# win = g.GraphWin("Triangle", plane['x_max'] * 2, plane['y_max'] * 2)
#
# # print(triangles[0].points[0][0] + plane['x_max'], triangles[0].points[0][1] + plane['y_max'])
# # print(triangles[0].points[1][0] + plane['x_max'], triangles[0].points[1][1] + plane['y_max'])
# # print(triangles[0].points[2][0] + plane['x_max'], triangles[0].points[2][1] + plane['y_max'])
#
# pt1 = g.Point(triangles[0].points[0][0] + plane['x_max'], triangles[0].points[0][1] + plane['y_max'])
# pt2 = g.Point(triangles[0].points[1][0] + plane['x_max'], triangles[0].points[1][1] + plane['y_max'])
# pt3 = g.Point(triangles[0].points[2][0] + plane['x_max'], triangles[0].points[2][1] + plane['y_max'])
#
# line1 = g.Line(pt1, pt2)
# line2 = g.Line(pt2, pt3)
# line3 = g.Line(pt3, pt1)
#
# line1.draw(win)
# line2.draw(win)
# line3.draw(win)
#
# win.getMouse()
#
# win.getMouse()
#
# win.close()

points = []
for i in range(3):
    pt = polygon.Point(0, 0)
    pt.random_point(plane)
    pt.insert_point(plane, points, i)
    print("exited...")
    print("")
    # points.append(pt)
    # print(points[i])

# t1 = polygon.Triangle(points)
# print(t1.t)
# t1.create_edges()
# t1.find_midpoint()
# print(t1.midpoints)


