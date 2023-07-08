import csv
import math
import numpy as np
from matplotlib import pyplot as plt


def main() -> None:
    filename = "fps.csv"
    average_data = read_csv_multiple(filename, 1)
    low_data = read_csv_multiple(filename, 2)
    print("test")
    plot_histo()


def read_csv_multiple(filename: str, n: int) -> dict[str, float]:
    filepath = filename
    data = {}
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            key = line[0]
            value = line[n]
            try:
                data[key] = float(value)
            except ValueError:
                data[key] = value
    return data


def plot_histo() -> None:
    fig = plt.figure()
    average_data = [21, 41, 41, 44, 45, 73, 46]
    low_data = [16, 29, 29, 30, 31, 55, 31]
    names = ["Native 4k", "TSR*", "XeSS", "FSR", "DLSS2", "DLSS3", "Native WQHD"]

    x = np.arange(len(names))

    # Width of each bar
    width = 0.2

    # Plotting the bars
    plt.bar(x - width / 2, average_data, width, label='Average')
    plt.bar(x + width / 2, low_data, width, label='1% Low')

    # Customizing the plot
    plt.xlabel('Upsampling Technique')
    plt.ylabel('FPS')
    title = 'Comparison of Upsampling Techniques in Cyberpunk 2077 with 4090'
    plt.title(title)
    plt.xticks(x, names)
    plt.legend()

    # Display the plot
    plt.show()

    title.replace(' ', '_')
    title.lower()
    path = "../images/" + "comparison"
    fig.savefig(path + ".png")


if __name__ == '__main__':
    main()
