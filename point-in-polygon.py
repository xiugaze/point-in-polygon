
def inside(points, target):

    x_sum = 0
    y_sum = 0
    for (x, y) in points:
        x_sum += x
        y_sum += y
    
    avg_point = (x_sum/len(points), y_sum/len(points))
    avg_slope = (avg_point[1] - target[1])/(avg_point[0] - target[0])

    edges = []


    for i in range(0, len(points) - 1):
        


        




        

    
