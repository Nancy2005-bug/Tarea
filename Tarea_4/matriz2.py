class Matrix:
    def __init__(self, matriz):
        self.m = matriz
        self.rows = len(matriz)
        self.cols = len(matriz[0])
        
    def __str__(self):
        return '\n'.join(['[' + '\t'.join(map(str, row)) + ']' for row in self.m])
    
    def mult(self, other):
        if self.cols != other.rows:
            raise ValueError("El número de columnas de la primera matriz debe coincidir con el número de filas de la segunda matriz.")
        result = [[0 for x in range(other.cols)] for x in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.m[i][k] * other.m[k][j]
        return Matrix(result)


m1=Matrix([[1,2,3],[4,5,6],[4,5,6]])
print(f"Matriz 1:\n{m1}\n")

m2=Matrix([[5,6,7],[2,3,4],[1,2,3]])
print(f"Matriz 2:\n{m2}\n")

m3=m1.mult(m2)
print(f"Matriz 1 x Matriz 2:\n{m3}\n")