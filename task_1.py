import math
import random

import numpy as np



def F(x):
    return sum(p_arr[i] for i in sorted(set(data)) if i < x)

def generate_random_array(length, min_value, max_value):

    return [random.randint(min_value, max_value) for _ in range(length)]

data = generate_random_array(10, -10, 10)
data_without_copies = sorted(set(data))
print("Выборка: ", data)

stat_arr = {i: data.count(i) for i in set(data)}
print("Статистический ряд: ", stat_arr)

p_arr = {i: stat_arr[i]/len(data) for i in data_without_copies}
print("Относительные частоты: ", p_arr)

m = sum(data) / len(data)
print("Мат. ожидание: ", m)

shit = 0
for i in data:
    shit += (i-m)**2
d = 1/(len(data)-1)*shit
print("Дисперсия: ", d)

print("СКО", math.sqrt(d))

print("Медиана: ", (len(data)+1)/2)

f_x = [F(i) for i in np.linspace(data[0]-0.5, data[-1]+0.5, 5000)]

print("\nF:")
print(f"0, при x <= {data_without_copies[0]}")
for i, val in enumerate(data_without_copies[1:]):
    summ = round(sum(p_arr[j] for j in data_without_copies[:i + 1]), 3)
    print(f"{summ}, при {data_without_copies[i]} < x <= {val}")
