import math
import random
import statistics

# import numpy as np

import graphs


# def F(x):
#     return sum(p_arr[i] for i in sorted(set(data)) if i < x)

def stats_m(arr):
    return sum(arr) / len(arr)

def stats_d(arr):
    shit = 0
    for i in arr:
        shit += (i - stats_m(arr)) ** 2
    return 1 / (len(data) - 1) * shit

def median_of_arrays(arrays):
    all_values = [value for array in arrays for value in array]
    all_values.sort()
    n = len(all_values)
    if n % 2 == 1:
        return all_values[n // 2]
    else:
        return (all_values[n // 2 - 1] + all_values[n // 2]) / 2

def generateSamples(sample_count, sample_capacity, min_value, max_value):
    return [[random.randint(min_value, max_value) for _ in range(sample_capacity)] for _ in range(sample_count)]

data = generateSamples(100, 100, -10, 10)

# статистика (матожидание)
statistics_m = [stats_m(i) for i in data]

# статистика (дисперсия)
statistics_d = [stats_d(i) for i in data]

# статистика (квантиль)
statistics_median = [statistics.median(i) for i in data]

graphs.draw_bar_chart(statistics_m, "", "")
graphs.draw_bar_chart(statistics_d, "", "")
graphs.draw_bar_chart(statistics_median, "", "")


print(statistics_m)
print(statistics_d)
print(statistics_median)

# # Пример использования функции:
# arrays = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# result = median_of_arrays(arrays)
# print(result)  # Выведет: 5
#
#
# # data_without_copies = sorted(set(data))
# print("Выборка: ", data)
#
# stat_arr = {i: data.count(i) for i in set(data)}
# print("Статистический ряд: ", stat_arr)
#
# p_arr = {i: stat_arr[i]/len(data) for i in data_without_copies}
# print("Относительные частоты: ", p_arr)
#
# m = sum(data) / len(data)
# print("Мат. ожидание: ", m)
#
# shit = 0
# for i in data:
#     shit += (i-m)**2
# d = 1/(len(data)-1)*shit
# print("Дисперсия: ", d)
#
# print("СКО", math.sqrt(d))
#
# print("Медиана: ", (len(data)+1)/2)
#
# f_x = [F(i) for i in np.linspace(data[0]-0.5, data[-1]+0.5, 5000)]
#
# print("\nF:")
# print(f"0, при x <= {data_without_copies[0]}")
# for i, val in enumerate(data_without_copies[1:]):
#     summ = round(sum(p_arr[j] for j in data_without_copies[:i + 1]), 3)
#     print(f"{summ}, при {data_without_copies[i]} < x <= {val}")
