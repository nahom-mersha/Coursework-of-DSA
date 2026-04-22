import random
import math
def monte_carlo_pi(num):
    inside = 0
    total_count = 0
    radius = 100

    for i in range(num):
        cx = random.uniform(-radius, radius)
        cy = random.uniform(-radius, radius)
        #we dont need square root cuze distance is always positive!!!!!
        distance_squared = cx**2 + cy**2
        if distance_squared <= radius**2:
            inside += 1
        total_count += 1

    return (inside / num) * 4


print(monte_carlo_pi(100))
print(monte_carlo_pi(1000))
print(monte_carlo_pi(10000))
print(monte_carlo_pi(100000))
print(math.pi)




# My initial Version was:
# import random
# import math
# def monte_carlo_pi(num):
#     inside_circle_list = 0
#     total_count = 0
#     outside_circle_list = 0
#     half_of_square_length = 5
#     radius = 1
#     object_length = 2

#     for i in range(num):
#         cx = random.randint(-radius, radius)
#         cy = random.randint(-radius, radius)
#         x1 = cx - half_of_square_length
#         x2 = cx + half_of_square_length
#         y1 = cy - half_of_square_length
#         y2 = cy + half_of_square_length
#         center = ((x1+x2)/2 , (y1+y2)/2)
#         distance = math.sqrt(center[0]**2 + center[1]**2)
#         if distance < radius:
#             inside_circle_list += 1
#         total_count += 1

#     return (inside_circle_list / total_count) * 4

# print(monte_carlo_pi(100))
# print(monte_carlo_pi(1000))
# print(monte_carlo_pi(10000))
# print(monte_carlo_pi(100000))
# print(math.pi)
