import csv
import math

with open('mobile_phones.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    count = 0

    for rows in reader:
        count += 1
    print(f'Всего строк {count}')

    csvfile.seek(0)
    three_g_rows = []
    count_tree_g = 0
    for row in reader:
        if row['three_g'] == '1':
            count_tree_g += 1
            three_g_rows.append(row)

    print(f'Количество телефонов, которые поддерживают 3-G: {count_tree_g}')

    csvfile.seek(0)
    dual_sim_rows = []
    count_sim = 0
    for row in reader:
        if row['dual_sim'] == '1':
            count_sim += 1
            dual_sim_rows.append(row)

    print(f'Количество телефонов, в которые можно вставить 2 сим-карты: {count_sim}')

    csvfile.seek(0)
    max_core_n = 0
    iter = 0
    for row in reader:
        if iter == 0:
            iter += 1
            continue
        iter += 1
        current_n = int(row['n_cores'])
        if current_n > max_core_n:
            max_core_n = current_n

    print(f'Максимальное количество ядер: {max_core_n}')

    csvfile.seek(0)
    n_cores_rows = []
    for row in reader:
        if row['n_cores'] == str(max_core_n):
            n_cores_rows.append(row)

    csvfile.seek(0)

    battery_power_sum = 0
    battery_power_rows = []
    iter = 0
    for rows in reader:
        if iter == 0:
            iter += 1
            continue
        battery_power_sum += int(rows['battery_power'])
        battery_power_rows.append(int(rows['battery_power']))
    sample_average = battery_power_sum/count
    print(f'Выборочное среднее: {sample_average}')

    # print(sample_average)
    # print(battery_power_rows)

    m_x = 0
    for x in  battery_power_rows:
        m_x += (x - sample_average)**2
    s_x = m_x/(count-1)
    print(f'Выборочная дисперсия: {s_x}')
    sko = math.sqrt(s_x)
    print(f'Среднее квадратичное отклонение: {sko}')

    median = (count+1)/2
    print(f'Выбораяная медиана: {median}')





    # for row in n_cores_rows:
    #     print(row)


