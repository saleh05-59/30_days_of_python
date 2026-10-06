# day 1 level 3

# part 1 examples

print(type(12))             # int
print(type(3.8))            # float
print(type(3+2j))           # complex
print(type("idk"))          # string
print(type(True))           # boolean
print(type([1, 2, 3]))      # list
print(type((1, 2, 3)))      # tuple
print(type({1, 2, 3}))      # set
print(type({'name':'idk'})) # dict

# part 2 euclidean distance
point_a = (2, 3)
point_b = (10, 8)
def euclidean_distance_formula(q_1, p_1, q_2, p_2) :
    return (((q_1-p_1)**2)+((q_2-p_2)**2)) ** (1/2)

print(euclidean_distance_formula(point_a[0],point_b[0],point_a[1],point_b[1]))
