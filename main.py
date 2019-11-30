import lib.points_generator as PO
import lib.polygon as polygon

def define_points(n):
    for i in range(n):
        points_list.append(PO.Point())
        # print("Setting point ....")
        points_list[i].set_point(plane)
        # print("Inserting point ....")
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

for i in range(10):
    triangles.append(polygon.Triangle())
    define_points(3)
    triangles[i].points = object_points[0:]
    del points_list[:]
    del object_points[:]
    print(triangles[i].points)

# t1 = polygon.Triangle(points)
# print(t1.t)
# t1.create_edges()
# t1.find_midpoint()
# print(t1.midpoints)


