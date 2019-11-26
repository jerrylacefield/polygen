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
    
# for i in points_list:
#     print(points_list[i])

# p1 = PG.Point()
# p2 = PG.Point()
# p3 = PG.Point()
#
# p1.set_point(plane)
# p1.insert_point(plane, points, p1)
#
# p2.set_point(plane)
# p2.insert_point(plane, points, p2)
#
# p3.set_point(plane)
# p3.insert_point(plane, points, p3)
#
# p1.print_point('A')
# p2.print_point('B')
# p3.print_point('C')

print(points)

# t1 = polygon.Triangle()
# t1.set_points(points)
# t1.print_points()


