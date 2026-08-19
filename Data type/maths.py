import math

# Function to calculate distance between two points
def distance(p1, p2):
    x1 = p1[0]
    y1 = p1[1]

    x2 = p2[0]
    y2 = p2[1]

    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return d


# Function to find farthest point from origin
def farthest_point(points):
    farthest = points[0]

    max_distance = distance(farthest, (0, 0))

    for point in points:
        d = distance(point, (0, 0))

        if d > max_distance:
            max_distance = d
            farthest = point

    return farthest


# Take number of points
n = int(input("Enter number of points: "))

points = []

# Take points as tuples
for i in range(n):
    x = int(input("Enter x coordinate: "))
    y = int(input("Enter y coordinate: "))

    point = (x, y)
    points.append(point)


# Display points
print("\nPoints:", points)


# Take two points for distance calculation
p1 = points[int(input("Enter index of first point: "))]
p2 = points[int(input("Enter index of second point: "))]

print("Distance between points:", distance(p1, p2))


# Find farthest point
print("Farthest point from origin:", farthest_point(points))