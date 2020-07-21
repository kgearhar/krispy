import numpy as np
import matplotlib.pyplot as plt
import random

# takes in list of result lists

def graph(results, names, save_location=None):
    bar_width = 1 / (len(results[0]) + 1)

    print(results)
    print(names)

    np_res = np.array(results)
    bar_matrix = np_res.transpose()
    
    r_array = []
    r_array.append(np.arange(len(bar_matrix[0])))

    for index in range(1, len(bar_matrix)):
        r_array.append([x + bar_width for x in r_array[index - 1]])

    print(r_array)
    
    for i in range(0, len(r_array)):
        randy_beans = [random.randint(0, 255) for x in range(3)]
        hex_code = f'#{randy_beans[0]:02x}{randy_beans[1]:02x}{randy_beans[2]:02x}'
        plt.bar(r_array[i], bar_matrix[i], width=bar_width, color=hex_code, edgecolor='white')


    labels = []
    labels.append('Orig. Results')
    if len(results) > 1:
        for name in names:
            labels.append(f'(-){name}')
        print(labels)
        ticks = [r + bar_width for r in range(len(results))]
        plt.title('n-1 Sensitivity Analysis')
    else:
        ticks = [bar_width]
        plt.title('Results')
    plt.xlabel('Trade Study Run', fontweight='bold')
    plt.xticks(ticks, labels)

    if save_location is None:
        plt.show()
    else:
        plt.savefig(save_location)


def test():
    test_data = [[1, 4, 3], [4, 6, 8]]
    names = ['peanut butter']
    graph(test_data, names, 'test.png')

if __name__ == '__main__':
    test()
