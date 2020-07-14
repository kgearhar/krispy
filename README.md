# krispy

[Github link](https://github.com/kgearhar/krispy.git)

## Matrix Operations

The following matrix operations are available to the user.

1. `Matrix(upper_right)` takes the upper right triangle of a matrix
	to create a matrix object.

2. `len(my_matrix)` will give you the length of the matrix

3. `str(my_matrix)` intuitive.

4. `Matrix.from_matrix_array(my_matrix)` this accepts a matrix instead of upper right array

5. `my_matrix.normalized()` gives you the normalized matrix

6. `my_matrix.eigenvector` will give you the eigenvector of your matrix

7. `my_matrix.consistency` gives you the calculated consistency value


## Getting Scores and Alternative Weights

1. `get_scores(criteria_eigenvector, tech_spec_eigenvector1, tech_spec_eigenvector2,...)`

2. `get_alternative_weights(criteria_eigenvector, tech_spec_eigenvector1, tech_spec_eigenvector2,...)`

## Graphing

1. To graph the data & save the image (for uploading) use 
	`graph(results, 'filename_for_saving.png')`

	You can send `graph` the original results, or the results from the sensitivity analysis.
	If you send JUST the original results, you'll need to wrap it in a list, i.e. `[results]`

## Sensitivity Analysis

1. `get_sensitivity(criteria_list, alt_weight_matrix)` will produce a list of results lists.
	can plug the array produced by `get_sensitivity()` into graph.

