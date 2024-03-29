import math
import random
import statistics

import numpy
import numpy as np

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


def stats_a(arr):
    sum = 0
    for i in arr:
        sum += (i - stats_m(arr)) ** 3
    central_moment = sum / len(arr)
    asymmetry = central_moment / math.sqrt(stats_d(arr)) ** 3
    return asymmetry


def stat_e(arr):
    sum = 0
    for i in arr:
        sum += (i - stats_m(arr)) ** 4
    central_moment = sum / len(arr)
    excess = central_moment / math.sqrt(stats_d(arr)) ** 4 - 3
    return excess


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


# def normalize_sample(sample, mean, variance):
#     return [(value - mean) / math.sqrt(variance) for value in sample]

def normalize(sample):
    arr = []
    m = stats_m(sample)
    d = stats_d(sample)
    for i in sample:
        arr.append((i - m) / math.sqrt(d))
    return arr


# data = generateSamples(100, 100, -10, 10)
n = 1000
lambd = 1.0
beta = 1 / lambd

data = np.random.exponential(beta, (n, n))

# data = numpy.random.standard_normal((100, 100))
# print(data)

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

normalized_m = normalize(statistics_m)
normalized_d = normalize(statistics_d)
print(normalized_m)
print(normalized_d)

graphs.draw_empiric_with_gamma(data)

# # Пример использования функции:
# arrays = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# result = median_of_arrays(arrays)
# print(result)  # Выведет: 5
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
