import csv
import math
import graphs


def quantile_calculation(data):
    sorted_data = sorted(data)
    position = 2 / 5 * len(sorted_data)

    if position.is_integer():
        quantile = sorted_data[int(position) - 1]
    else:
        lower_index = int(position) - 1
        upper_index = int(position)
        lower_value = sorted_data[lower_index]
        upper_value = sorted_data[upper_index]
        quantile = (lower_value + upper_value) / 2

    print(f'Квантиль порядка 2/5: {quantile}')


def calculate_sample_parameters(data):
    sample_average = sum(data) / len(data)
    print(f'Выборочное среднее: {sample_average}')

    m_x = 0
    for x in data:
        m_x += (x - sample_average) ** 2
    s_x = m_x / (len(data) - 1)
    print(f'Выборочная дисперсия: {s_x}')
    sko = math.sqrt(s_x)
    print(f'Среднее квадратичное отклонение: {sko}')

    n = len(data)
    sorted_sample = data
    sorted_sample.sort()

    if n % 2 == 0:
        median1 = sorted_sample[n // 2]
        median2 = sorted_sample[n // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = sorted_sample[n // 2]
    print(f'Выборачная медиана: {median}')

    stat_arr = {i: sorted(data).count(i) for i in set(sorted(data))}
    data_without_copies = sorted(set(data))
    p_arr = {i: stat_arr[i] / len(data) for i in data_without_copies}

    quantile_calculation(data)

    graphs.draw_empiric_func(data, "ёмкость аккумулятора", "Эмпирическая функция распределения")
    graphs.draw_gistogram_without_frequency(data, "ёмкость аккумулятора", "Частота")
    graphs.draw_box_diagram(data, "ёмкость аккумулятора", " ")


def phone_counter(reader, string):
    csvfile.seek(0)
    count = 0
    for row in reader:
        if row[string] == '1':
            count += 1
    return count


def column_values(reader, string):
    csvfile.seek(0)
    iterator = 0
    array = []
    for rows in reader:
        if iterator == 0:
            iterator += 1
            continue
        array.append(int(rows[string]))
    return array


def find_wifi_data(reader, string1, string2, availability):
    csvfile.seek(0)
    iterator = 0
    array = []
    for rows in reader:
        if iterator == 0:
            iterator += 1
            continue
        if rows[string2] == str(availability):
            array.append(int(rows[string1]))
    return array


with open('mobile_phones.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    three_g_count = phone_counter(reader, 'three_g')
    print(f'Количество телефонов, которые поддерживают 3-G: {three_g_count}')

    dual_sim_count = phone_counter(reader, 'dual_sim')
    print(f'Количество телефонов, в которые можно вставить 2 сим-карты: {dual_sim_count}')

    max_core_n = max(column_values(reader, 'n_cores'))
    print(f'Максимальное количество ядер: {max_core_n}')
    print()

    data = column_values(reader, 'battery_power')
    calculate_sample_parameters(data)
    print()
    data_with_wifi = find_wifi_data(reader, 'battery_power', 'wifi', 1)
    print(data_with_wifi)
    calculate_sample_parameters(data_with_wifi)
    print()
    data_without_wifi = find_wifi_data(reader, 'battery_power', 'wifi', 0)
    print(data_without_wifi)
    calculate_sample_parameters(data_without_wifi)
