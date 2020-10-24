import numpy as np
import math

class GaussJordan:

    def __init__(self,matrix):

        for i in range(len(matrix)):
            matrix[i] = np.array(matrix[i], dtype=float)
        matrix = np.array(matrix, dtype=float)
        self.matrix = matrix

    def solution(self):

        matrix = self.matrix
        columns = len(matrix[0])-1
        rows = len(matrix)

        for c in range(columns):
            if c>=rows: return matrix
            if matrix[c][c] == 0:
                for cont in range(c+1,rows):
                    if matrix[cont][c] != 0:
                        cM = matrix[c]
                        contM = matrix[cont]
                        for aux in range(len(matrix)):
                            if aux == c:
                                matrix[aux] = cM
                            elif aux == cont:
                                matrix[aux] = contM
                        break
            if matrix[c][c] == 0:
                if c != columns-1:
                    continue
                else:
                    return matrix
            matrix[c] = matrix[c]/matrix[c][c]
            print(matrix)
            for r in range(rows):
                if r != c:
                    matrix[r] = matrix[r] - matrix[r][c] * matrix[c]

        return matrix

print(GaussJordan([["0","1","1","6"],["1","-2","-1","4"],["1","-1","1","5"]]).solution())
