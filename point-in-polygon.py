# The intersection function returns the point of intersection between the
# line that is made from p1 and p0 and the horizontal line y.
def intersection(p1, p0, y):
    return (y * (p1[0] - p0[0]) - p0[1] * (p1[0] - p0[0]) - p0[0] * (p1[1] - p0[1])) / (p1[1] - p0[1])


# The inside function determines if a point is inside a polygon made of other points.
def inside(points, target):
    count = 1 if points[0][1] == target[1] else 0
    max_x = points[0][0]
    # Finds the bounds that the intersections must be made in.
    for p in points:
        max_x = p[0] if max_x < p[0] else max_x
        count = count + 1 if p[1] == target[1] else count
    # min_x is the x value of the target point.

    # A point is within the polygon if the number of intersections
    # within the bounds is an odd number. This is accomplished by a
    # series of function calls.

    # The filter function will remove all points that do not have
    # intersections within the bounds. The filter function also returns
    # an iterator which must be converted into a list before the remaining
    # elements can be counted. If the length is odd, then return true.
    return (count + len(list(filter(
        # This lambda function is used by the filter to iterate through all
        # lines created by the points within the points list and to check if
        # the intersection with the horizontal line y is within bounds.
        # If it is, the point is kept within the array.
        lambda i: (target[0]
                   <= intersection(points[i], points[(i + 1) % len(points)], target[1])
                   <= max_x),
        range(len(points))
    ))) % 2) == 1


print(inside([(2, 3), (5, 7), (8, 5), (6, 2), (4, 1)], (2, 4)))
