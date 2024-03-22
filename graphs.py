import matplotlib.pyplot as plt
import numpy as np
import scipy
import seaborn as sns
from scipy.stats import *


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
def draw_gistogram_without_frequency(data, x_text, y_text):
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=20, alpha=0.6)
    plt.xlabel(x_text)
    plt.ylabel(y_text)
    plt.show()
    return


# Гистограмма
def draw_bar_chart(data, x_text, y_text):
    # plt.subplots_adjust(hspace=0.5)
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=20, density=True, alpha=0.6)
    mu, std = norm.fit(data)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    plt.xlabel(x_text)
    plt.ylabel(y_text)
    plt.show()
    return


# Box-plot
def draw_box_diagram(data, x_text, y_text):
    # plt.subplots_adjust(hspace=0.5)
    plt.figure(figsize=(8, 6))
    plt.boxplot(data)
    plt.xlabel(x_text)
    plt.ylabel(y_text)
    plt.show()


def draw_empiric_with_gamma(sample):
    np.random.seed(0)
    print("draw-empiric")
    sorted_samples = [np.sort(i) for i in sample]
    x_arr = [i[1] for i in sorted_samples]
    # print(x_arr)

    x_arr = np.sort(x_arr)
    empiric = expon.cdf(x_arr, scale=1)
    print(empiric)
    # print(empiric)
    for i in range(0, len(empiric)-1):
        empiric[i] = empiric[i]*len(sample)

    plt.hist(empiric, bins=len(x_arr), density=True, histtype='step', label='Empirical CDF')

    gamma_x = np.arange(0, 12, 0.001)
    gamma_y = scipy.stats.gamma.pdf(gamma_x, 2)
    plt.plot(gamma_x, gamma_y)
    plt.xlabel('X')
    # plt.title('Empirical Cumulative Distribution Function (CDF)')
    plt.legend()
    plt.grid(True)
    plt.show()

