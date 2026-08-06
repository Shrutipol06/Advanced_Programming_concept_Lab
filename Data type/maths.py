import math

# 1. Function to calculate Euclidean distance between two points: (x1, y1) and (x2, y2)
def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    # Distance formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# 2. Function to find the point farthest from the origin (0, 0)
def find_farthest_from_origin(points_list):
    if not points_list:
        return None
    
    origin = (0, 0)
    farthest_point = points_list[0]
    max_distance = calculate_distance(origin, farthest_point)
    
    for point in points_list[1:]:
        current_distance = calculate_distance(origin, point)
        if current_distance > max_distance:
            max_distance = current_distance
            farthest_point = point
            
    return farthest_point, max_distance


# --- DEMO / MAIN PROGRAM ---

# List of 2D points represented as (x, y) tuples
points = [
    (1, 2),
    (5, -3),
    (-8, 6),
    (0, 4),
    (7, 1)
]

print("List of points:", points)

# Task 1: Calculate distance between two specific points
p1 = points[0]  # (1, 2)
p2 = points[1]  # (5, -3)
dist_between_p1_p2 = calculate_distance(p1, p2)

print(f"\n1. Distance between {p1} and {p2}: {dist_between_p1_p2:.2f}")

# Task 2: Find the point farthest from the origin (0, 0)
farthest, distance_from_origin = find_farthest_from_origin(points)

print(f"2. Farthest point from (0, 0) is {farthest} with a distance of {distance_from_origin:.2f}")