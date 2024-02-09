# The intersection function returns the point of intersection between the
# line that is made from p1 and p0 and the horizontal line y.
def intersection(p1, p0, y):
    return (y * (p1[0] - p0[0]) - p0[1] * (p1[0] - p0[0]) - p0[0] * (p1[1] - p0[1])) / (p1[1] - p0[1]), y


# The in_bounds function returns true if the point is in the bounds
def in_bounds(bounds, point):
    return bounds['min_y'] <= point[1] <= bounds['max_y'] and bounds['min_x'] <= point[0] <= bounds['max_x']


# The inside function determines if a point is inside a polygon made of other points.
def inside(points, target):
    # Finds the bounds that the intersections must be made in.
    min_y = min(points, key=lambda p: p[1])[1]
    max_y = max(points, key=lambda p: p[1])[1]
    max_x = max(points, key=lambda p: p[0])[0]
    # min_x is the x value of the target point.

    # A point is within the polygon if the number of intersections
    # within the bounds is an odd number. This is accomplished by a
    # series of function calls.

    # The filter function will remove all points that do not have
    # intersections within the bounds. The filter function also returns
    # an iterator which must be converted into a list before the remaining
    # elements can be counted. If the length is odd, then return true.
    return len(list(filter(
        # This lambda function is used by the filter to iterate through all
        # lines created by the points within the points list and to check if
        # the intersection with the horizontal line y is within bounds.
        # If it is, the point is kept within the array.
        lambda i: in_bounds(
            {'min_y': min_y, 'min_x': target[0], 'max_y': max_y, 'max_x': max_x},
            intersection(
                points[i],
                points[(i + 1) % len(points)],
                target[1]
            )
        ),
        range(len(points))
    ))) % 2 == 1


print(inside([(2, 3), (5, 7), (8, 5), (6, 2), (4, 1)], (100, 100)))
