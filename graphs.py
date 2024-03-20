import matplotlib.pyplot as plt
import numpy as np
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
    
def draw_empiric_with_theoretical_values(sample):
    np.random.seed(0)

    sorted_samples = [np.sort(i) for i in sample]

    # Calculate the empirical CDF
    x = [i[1] for i in sorted_samples]  # Considering the second element as the argument
    y = [np.sum(i <= j) / len(j) for i, j in zip(sorted_samples, sample)]

    # Calculate the theoretical CDF using stats.expon.cdf
    x_theoretical = np.linspace(0, np.max([np.max(i) for i in sorted_samples]), 1000)
    y_theoretical = expon.cdf(x_theoretical, scale=1)

    # Plotting
    plt.figure(figsize=(8, 6))
    for i in range(len(sample)):
        plt.plot(x[i], y[i], marker='o', markersize=8, linestyle='None', label=f'Sample {i+1} Empirical CDF at x={x[i]}')
    plt.plot(x_theoretical, y_theoretical, linestyle='--', color='r', label='Theoretical CDF')
    plt.xlabel('X')
    plt.ylabel('Cumulative Probability')
    plt.title('Empirical Cumulative Distribution Function (CDF)')
    plt.legend()
    plt.grid(True)
    plt.show()

def shit(data, x_text, y_text):
    # plt.subplots_adjust(hspace=0.5)
    plt.plot(np.sort(data), np.arange(len(data)) / len(data))
    plt.plot(np.linspace(0, data, 1000), expon.cdf())

    plt.figure(figsize=(8, 6))
    plt.step(sorted(data), np.arange(len(data)) / len(data))
    plt.xlabel(x_text)
    plt.ylabel(y_text)
    # plt.xlabel("ИМТ")
    # plt.ylabel("Эмпирическая функция распределения")
    plt.show()
