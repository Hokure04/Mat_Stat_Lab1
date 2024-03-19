import csv

with open('mobile_phones.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

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

    for row in n_cores_rows:
        print(row)




def sample_average(file, string):
    count = 0
    for row in reader:
        count += 1

    csvfile.seek(0)
    battery_power_sum = 0
    iter = 0
    for row in reader:
        if iter == 0:
            iter += 1
            continue
        battery_power_sum += int(row[string])

