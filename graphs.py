import matplotlib.pyplot as plt
import numpy as np

# Эмпирическая функция распределения
def draw_empiric_func(data, x_text, y_text):
    # plt.subplots_adjust(hspace=0.5)
    plt.figure(figsize=(8, 6))
    plt.step(sorted(data), np.arange(len(data)) / len(data))
    plt.xlabel(x_text)
    plt.ylabel(y_text)
    # plt.xlabel("ИМТ")
    # plt.ylabel("Эмпирическая функция распределения")
    plt.show()

# Гистограмма
def draw_bar_chart(data, x_text, y_text):
    # plt.subplots_adjust(hspace=0.5)
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=20)
    plt.xlabel(x_text)
    plt.ylabel(y_text)
    # plt.xlabel("ИМТ")
    # plt.ylabel("Частота")
    plt.show()
    return

# Box-plot
def draw_box_diagram(data, x_text, y_text):
    # plt.subplots_adjust(hspace=0.5)
    plt.figure(figsize=(8, 6))
    plt.boxplot(data)
    plt.xlabel(x_text)
    plt.ylabel(y_text)
    # plt.xlabel("Все наблюдатели")
    # plt.ylabel("ИМТ")
    plt.show()
