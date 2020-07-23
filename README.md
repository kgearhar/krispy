# krispy

[Github link](https://github.com/kgearhar/krispy.git)

## Matrix Operations (Matrix class)

The following matrix operations are available to the user. (Suppose we import krispy as kp)

1. `Matrix(upper_right)` takes the upper right triangle of a matrix as a list, e.g. [1, 3, 6]
	to create a matrix object.
```python
my_matrix = kp.Matrix(upper_right_list)
``` 
Now that we have a matrix, we can perform matrix calculations on my_matrix.

2. `len(my_matrix)` will give you the length of the matrix. (This is like height)

3. `str(my_matrix)` will give you the matrix as a string (for printing purposes). 

4. `Matrix.from_matrix_array(my_matrix)` this accepts a matrix instead of upper right array. This is particularly useful if you already have a built matrix in your code and just need the eigenvector or consistency.

5. `.normalized()` gives you the normalized matrix
```python
my_norm_matrix = my_matrix.normalized()
```

6. `.eigenvector` will give you the eigenvector of your matrix. This is a **property** so we don't need parentheses.
```python
my_eigenvec = my_matrix.eigenvector
```

7. `.consistency` gives you the calculated consistency value. This is a **property** so we don't need parentheses.
```python
c_value = my_matrix.consistency
```


## Getting Scores and Alternative Weights

1. `.get_scores(criteria_eigenvector, tech_spec_eigenvector1, tech_spec_eigenvector2,...)`

	You can use this function to calculate the overall results of the trade study. Notice that `get_scores` takes in a variable number of arguments but **the criteria eigenvector comes first**. 
	
	Suppose you have `criteria_eig` and a list of all the eigenvectors `eigenmatrix = [eig1, eig2, eig3,...,eign]`  and you want to calculate the results. Then you can call `get_scores` like this:
	
```python
results = kp.get_scores(criteria_eig, *eigenmatrix)
```
The asterisk in front of `eigenmatrix` **unpacks** everything in there so that we're sending a variable number of lists instead of a list of lists.
	
`.get_scores` will return a list of scores, e.g. `[.42, .22, .21, .12]`.
	
2. `.get_alternative_weights(criteria_eigenvector, tech_spec_eigenvector1, tech_spec_eigenvector2,...)`

	You can use this function to get **just the alternative weights** as a matrix. This is useful for calling the `sensitivity` function. 
	
	Suppose you have `criteria_eig` and a list of all the eigenvectors `eigenmatrix = [eig1, eig2, eig3,...,eign]` 
	and you want to calculate the alternative weights. Then you can call `get_alternative_weights` like this:
	
```python
results = kp.get_alternative_weights(criteria_eig, *eigenmatrix)
```
 The asterisk in front of `eigenmatrix` **unpacks** everything in there so that we're sending a variable number of lists instead of a list of lists.
	
## Graphing

1. `.graph(results, names, 'filename_for_saving.png')`

  There are two different uses for `graph`. 

  1. The first usage is for getting the initial graph of the results. For this usage, we want to send the results wrapped in a list. So if you have `results = [.42, .22, .21, .12]`, then you want to wrap this in a list...i.e. `wrapped_results = [results]`.

   You also want to send **the list of the names of the alternatives**. If we are comparing cheese, an example names list would be `names = ['pepper jack', 'cheddar', 'swiss', 'stilton']`.

   Finally, give a save location. An example of this would be `save_loc = '/images/result_graph.png'`.

   Thus your function call would be:
```python
kp.graph(wrapped_results, names, save_loc)
```

  2. The second usage is for getting the graph of the sensitivity analysis data.  For this usage, we want to send the results of the sensitivity analysis. The sensitivity analysis will send back a list of lists like this `sens_results = [[1, 4, 2], [3, 6, 9], [4, 2, 2], [5, 8, 1]]`. 

  We also want to send **the list of the names of the tech specs or criteria**. If this trade study is about cheese, and exmaple name list would be `names = ['cost', 'flavor', 'odor', 'texture']`.

  Finally, give a save location. An example of this would be `save_loc = '/images/sens_result_graph.png'`.

  Thus your function call would be:
```python
kp.graph(sens_results, names, save_loc)
```

## Sensitivity Analysis

1. `get_sensitivity(criteria_list, alt_weight_matrix)` will produce a list of lists. Each list represents
	a run of the trade study, but remember, we remove each criterion for the runs to see if the results change.
	An example: `[[1, 4, 2], [3, 6, 9], [4, 2, 2], [5, 8, 1]]`. 
	
	If you want to calculate the sensitivity analysis results, first save the `criteria_list`. Next,
	you need to get a matrix of the alternative weights (a matrix is a list of lists). To do this, make an `alt_weight_matrix`
	variable and call `get_alternative_weights` (explained above).
	
```python
sens_results = kp.get_sensitivity(criteria_list, alt_weight_matrix)
```

Thank you for reading through this! Don't hesitate to reach out to me to ask questions. 

If you are not Hayden, then I ask that you buy me a hot tea, kava, or GF/DF muffin if we ever meet in person
and you have used krispy.
