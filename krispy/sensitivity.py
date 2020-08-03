import math

import numpy as np

from .graph import graph
from .matrix import Matrix

# now we need the ability to calc results & alt weight (jacked from other file) ************

def _multiply(priority_weight, alt_weight_matrix):
    results = []

    for alt_weight in alt_weight_matrix:
        results.append(sum(x_i*y_i for x_i, y_i in zip(priority_weight, alt_weight)))
    return results


# now for what you actually call to get the sensitivity analysis ***************************

def get_sensitivity(criteria_list, alt_weight_matrix):
    varying_results = []

    # add the original results
    original_matrix = Matrix(criteria_list)
    varying_results.append(_multiply(original_matrix.eigenvector, alt_weight_matrix))

    # now we add the new results
    for i in range(len(alt_weight_matrix[0])):

        shrunken_criteria_matrix = original_matrix._remove_row(i)
        shrunken_priority = shrunken_criteria_matrix.eigenvector


        #shrunk_alt = alt_weight_matrix.pop(i)
        shrunk_alt = np.array(alt_weight_matrix)
        shrunk_alt = shrunk_alt.transpose()
        shrunk_alt = np.delete(shrunk_alt, i, 0)
        shrunk_alt = shrunk_alt.transpose()
        varying_results.append(_multiply(shrunken_priority, shrunk_alt))
    
    return varying_results



# testing, test, 1 2 3 *********************************************************************
def test():
    criteria_list = [1, 5, 3, 9, 5, 3, 9, (1/3), 3, 3]

    alt_weight_matrix = [[0.3, 0.1927, 0.2265, 0.3249, 0.3698],
                        [0.3, 0.256, 0.4254, 0.21,  0.1433],
                        [0.1, 0.3247, 0.138, 0.177, 0.2247],
                        [0.3, 0.2266, 0.2101, 0.2881, 0.2622]]

    results = get_sensitivity(criteria_list, alt_weight_matrix)
    print('All the results\n')

    print(results)
    graph(results, ['peanut butter', 'kava', 'beard', 'leather', 'father'])

if __name__ == '__main__':
    test()
