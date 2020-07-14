import math
import copy
import numpy as np

# all of the matrix algorithms *****************************************

class Matrix:
    def __init__(self, data=None):
        if data is None:
            # Special case trivial matrix
            self.built_matrix = [[0]]
        else:
            # Build from upper triangle
            self.built_matrix = self._build_matrix(data)

    def __len__(self):
        return len(self.built_matrix)
    
    def __str__(self):
        return str(self.built_matrix)

    @classmethod
    def from_matrix_array(cls, matrix):
        new_matrix = cls()
        new_matrix.built_matrix = np.array(matrix)
        return new_matrix


    def _remove_row(self, id_of_objective):
        my_matrix = self.built_matrix
        # now let's suck out an objective -> make it a list
        new_list = []
        for i in range(0, len(self)):
            for j in range(0, len(self)):
                if i != id_of_objective and j != id_of_objective:
                    new_list.append(my_matrix[i][j])

        new_num_row = len(self) -1
        # now make it a matrix
        new_matrix = np.ones((new_num_row, new_num_row))
        for i in range(0, new_num_row):
            for j in range(0, new_num_row):
                new_matrix[i][j] = new_list.pop(0)
        return Matrix.from_matrix_array(new_matrix)
        

    def _build_matrix(self, up_triangle):
        # Determine number of rows from number of elements in the
        # upper triangle
        top_right = up_triangle[:]
        t = len(top_right)
        num_row = round((1 + math.sqrt(1+8*t))/2)

        bottom_left = [1 / x for x in top_right]
        criteria_matrix = np.ones((num_row, num_row))

        for i in range(0, num_row - 1):
            for j in range(i+1, num_row):
                criteria_matrix[i][j] = top_right.pop(0)
                criteria_matrix[j][i] = bottom_left.pop(0)

        return criteria_matrix
    
    def _column_sums(self):
        sum_vec = []
        for i in range(0, len(self)):
            sum_vec.append(sum(self.built_matrix[:,i])) # "our_matrix[:,i]" just means everything in the i'th column
        return sum_vec


    def normalized(self):
        my_matrix = copy.deepcopy(self.built_matrix)
        for i in range(0, len(self)):
            current_column = self.built_matrix[:,i] 
            current_column = [x / sum(current_column) for x in current_column] 
            my_matrix[:,i] = current_column 
        
        return Matrix.from_matrix_array(my_matrix)

    def _calc_eigenvector(self):
        e_vec = []

        for i in range(0, len(self)):
            current_row = self.built_matrix[i,:]
            e_vec.append(sum(current_row)/len(self))
        return e_vec
    
    def _calc_max_eigenvalue(self, sum_vec, eigenvec):
        return sum(x_i*y_i for x_i, y_i in zip(sum_vec, eigenvec))
    
    def consistency_check(self, max_eig):
        return ((max_eig - len(self)) / (len(self) -  1))

    @property
    def eigenvector(self):
        normalized_matrix = self.normalized()
        eigenvec = normalized_matrix._calc_eigenvector()
        return eigenvec

    @property
    def consistency(self):
        sum_vec = self._column_sums()
        eigenvec = self.eigenvector
        max_eig = self._calc_max_eigenvalue(sum_vec, eigenvec)
        consistency_val = self.consistency_check(max_eig)
        return consistency_val
    


