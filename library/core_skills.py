import random

rand_list = [random.randint(1, 20) for _ in range(10)]

print(rand_list)

# Filter Numbers Below 10 (List Comprehension)

filtered_rand_list_lc = [x for x in rand_list if x < 10]

print(filtered_rand_list_lc)

# . Filter Numbers Below 10 (Using filter)

filtered_list = list(filter(lambda x: x < 10, rand_list))

print(filtered_list)
