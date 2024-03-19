import math
import matplotlib.pyplot as plt
import numpy as np


def print_arr(arr):
    print(" ".join(map(str, arr)))


input_data = [0.90, -1.00, 0.24, 0.62, 0.55,
              -1.45, -1.45, -0.52, 0.17, -1.31,
              -0.56, 1.45, 1.45, 0.54, 0.86,
              -1.73, -0.22, -0.64, -0.91, 1.45]

print("Исходные данные:")
print_arr(input_data)

# Вариационный ряд (все элементы в порядке возрастания)
data = sorted(input_data)
print("Вариационный ряд:")
print_arr(data)
print()

# Описательная статистика
min_value = min(data)
max_value = max(data)
range_value = max_value - min_value

print("Минимальное значение: ", min_value)
print("Максимальное значение: ", max_value)
print("Размах выборки: ", range_value)
print()

# Частотное распределение
stat_arr = {i: data.count(i) for i in set(data)}
print("Статистический ряд: " , stat_arr)
data_without_copies = sorted(set(data))
# Относительные частоты
p_arr = {i: stat_arr[i] / len(data) for i in data_without_copies}
print("Относительные частоты: ", p_arr)

# Мат.ожидание значение на частоту
M = sum(i * p_arr[i] for i in data_without_copies)
# Выборочная Дисперсия (квадрат значения на частоту)
D = sum(i**2 * p_arr[i] for i in data_without_copies) - M**2
# Исправленная дисперсия (С.К.0 Среднеквадратичное отклонение)
NEW_D = D * len(data) / (len(data) - 1)
# СКО
std_deviation = math.sqrt(D)
#Исправленное СКО
new_std_deviation = math.sqrt(D**2)

print("Математическое ожидание: ", round(M, 7))
print("Дисперсия: ", round(D, 7))
print("Исправленная дисперсия: ", round(NEW_D, 7))
print("Среднеквадратичное отклонение: ", std_deviation)
print("Исправленное среднеквадратичное отклонение: ", new_std_deviation)


# Эмпирическая функция распределения
def F(x):
    return sum(p_arr[i] for i in data_without_copies if i < x)


print("\nF:")
print(f"0, при x <= {data_without_copies[0]}")

for i, val in enumerate(data_without_copies[1:]):
    summ = round(sum(p_arr[j] for j in data_without_copies[:i + 1]), 3)
    print(f"{summ}, при {data_without_copies[i]} < x <= {val}")

# Интервальная статистика
print('\nИнтервальный статистический ряд:')
#Считаем по формуле Стерджеса
h = round((data_without_copies[-1] - data_without_copies[0]) / (1 + math.log2(len(data))), 1)

print('Величина интервала h = ', h)
#Начало первого интервала
start = data_without_copies[0] - h / 2
# Конечное значение интервала
finish = start + h
# Массив для середин интервалов
arr_fr1 = []
# Массив для относительных частот
arr_fr2 = []
# Инициализация счетчика для частоты в текущем интервале
num = 0

# Цикл по уникальным значениям выборки
for i in data_without_copies:
    # Проверка, принадлежит ли текущее значение интервалу
    if i < finish:
        # Увеличение счетчика частоты
        num += stat_arr[i]
    else:
        # Добавление середины интервала и относительной частоты в массивы
        arr_fr1.append((start + finish) / 2)
        arr_fr2.append(num / len(data))
        # Вывод информации о текущем интервале
        print("[", round(start, 4), ", ", round(finish, 4), "): частота: ", num, " частотность: ", num / len(data))
        # Сброс счетчика и обновление границ интервала
        num = 0
        start = finish
        finish = start + h
        num += stat_arr[i]

# Добавление информации о последнем интервале после завершения цикла
arr_fr1.append((start + finish) / 2)
arr_fr2.append(num / len(data))
print("[", start, ", ", finish, "): частота: ", num, " частотность: ", num / len(data))

x = np.linspace(data[0] - 0.5, data[-1] + 0.5, 5000)
y = [F(i) for i in x]

# График
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x, y, 'b')

# Подграфик 1: График эмпирической функции распределения (ЭФР)
ax.plot(x, y, 'b')  # Построение графика ЭФР. 'b' указывает цвет линии (синий).
ax.set_xlabel('Значения выборки')  # Подпись оси x.
ax.set_ylabel('Эмпирическая функция распределения')  # Подпись оси y.

plt.show()

# Подграфик 2: Гистограмма интервального статистического ряда
fig, ax = plt.subplots()
ax.bar(arr_fr1, arr_fr2, color='lightblue')
plt.plot(arr_fr1, arr_fr2, marker="o")

# Подписи осей и графика
ax.set_xlabel('Интервалы')
ax.set_ylabel('Относительные частоты')

# Отображение гистограммы
plt.show()