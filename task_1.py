import random
def generate_random_array(length, min_value, max_value):

    return [random.randint(min_value, max_value) for _ in range(length)]

random_arr = generate_random_array(10, -10, 10)
print(random_arr)