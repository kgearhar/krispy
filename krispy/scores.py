import numpy as np


def get_scores(*args):
    return _calculate_scores_and_weights(True, *args)

def get_alternative_weights(*args):
    return _calculate_scores_and_weights(False, *args)


# compute alternative weight matrix and priority weight
def _calculate_scores_and_weights(return_results, *args):
    priority_weight = list(args)[0]

    eigenmatrix = []
    for arg in args:
        eigenmatrix.append(list(arg))
    eigenmatrix.pop(0)

    numpy_egg = np.array(eigenmatrix)
    alt_weight_matrix = numpy_egg.transpose()

    results = []
    for alt_weight in alt_weight_matrix:
        results.append(sum(x_i*y_i for x_i, y_i in zip(priority_weight, alt_weight)))
    
    # just want the results
    if return_results:
        return results
    
    # just want the alternative weight matrix for the sensitivity analysis
    else:
        return alt_weight_matrix



