import lib.points_generator as PG
import lib.polygon as polygon

plane = {'x_max':0, 'y_max':0,'x_min':0,'y_min':0}

points = []
points_list = []

PG.coordinate_plane(plane)

for i in range(3):
    points_list.append(PG.Point())
    points_list[i].set_point(plane)
    points_list[i].insert_point(plane, points, points_list[i])

print(points)

# t1 = polygon.Triangle()
# t1.set_points(points)
# t1.print_points()


