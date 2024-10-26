class matrix:
    """
    Matrices :b   
    """
    def __init__(self, matriz):
        self.m = matriz
        self.rows = len(matriz)
        self.cols = len(matriz[0])
        
    def __str__(self):
        return "\n".join(["[" + "  ".join(str(num) for num in row) + "]" for row in self.m])
    
    def __repr__(self):
        return f"matrix({self.m})"    
    
    def __getitem__(self, index):
        if isinstance(index, tuple) and len(index) == 2:
            i, j = index
            return self.m[i][j]
        return self.m[index]
    
    def __setitem__(self, index, value):
        if isinstance(index, tuple) and len(index) ==2:
            i, j = index
            self.m[i][j] = value
        else:
            self.m[index] = value        
    
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("El número de filas y columnas no coincide.")
        result = [[self.m[i][j] + other.m[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return matrix(result)
    
    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("El número de filas y matrices no coincide.")
        result = [[self.m[i][j] - other.m[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return matrix(result)
    
    def __mul__(self, other):
        if isinstance(other, matrix):
            if self.cols != other.rows:
                raise ValueError("Estas matrices no se pueden multiplicar.")
            result = [[sum(a*b for a,b in zip(self.m_row, other.m_col)) for other.m_col in zip(*other.m)] for self.m_row in self.m]
            return matrix(result)
        elif isinstance(other, (int, float)):
            result = [[num * other for num in row] for row in self.m]
            return matrix(result)
        else:
            raise ValueError("No se pudo realizar la multiplicación.")
        
    def __call__(self, other):
        return self.__mul__(other)
        
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            result = [[num * other for num in row] for row in self.m]
            return matrix(result)
        else:
            raise ValueError("No se pudo realizar la multiplicación.")    
    
    def transpuesta(self):
        result = [[self.m[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return matrix(result)
    
    def __pow__(self, exponent):
        """
        Potencias de matrices.
        """
        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError("El exponente debe ser un número real.")    
        result = matrix([[1 if i == j else 0 for j in range(self.cols)] for i in range(self.rows)])    
        for _ in range(exponent):
            result = result * self    
        return result
    
    def __neg__(self):
        """
        Multiplica todos los elementos de la matriz por -1.
        """
        result = [[-num for num in row] for row in self.m]
        return matrix(result)
    
    def __abs__(self):
        """
        Valor absoluto de una matriz.
        """
        result = [[abs(num) for num in row] for row in self.m]
        return matrix(result)
    
    def __eq__(self, other):
        """
        Igualar dos matrices.
        """
        if not isinstance(other, matrix):
            return False
        return self.m == other.m
    
    def gauss_jordan(self):
        """
        Aplica el método de Gauss-Jordan para llevar la matriz a su forma escalonada reducida (RREF).
        """
        mat = [row[:] for row in self.m]  # Hacemos una copia de la matriz para no modificar la original
        n = self.rows
        m = self.cols
        
        for i in range(n):
            # Buscamos el máximo en la columna i para hacer un pivoteo parcial
            max_row = max(range(i, n), key=lambda r: abs(mat[r][i]))
            mat[i], mat[max_row] = mat[max_row], mat[i]  # Intercambiamos filas
            
            # Hacemos que el pivote sea 1
            pivot = mat[i][i]
            if pivot != 0:
                mat[i] = [x / pivot for x in mat[i]]
            
            # Hacemos que todos los elementos de la columna i (excepto el pivote) sean 0
            for j in range(n):
                if j != i:
                    factor = mat[j][i]
                    mat[j] = [mat[j][k] - factor * mat[i][k] for k in range(m)]
        
        return matrix(mat)
    
    def inverse(self):
        """
        Inversa de la matriz usando el método de Gauss-Jordan.
        """
        if self.rows != self.cols:
            raise ValueError("Solo se pueden invertir matrices cuadradas.")
        
        # Creamos la matriz identidad del mismo tamaño
        identity = [[1 if i == j else 0 for j in range(self.cols)] for i in range(self.rows)]
        
        # Construimos la matriz aumentada [A|I]
        augmented_matrix = [self.m[i] + identity[i] for i in range(self.rows)]
        augmented = matrix(augmented_matrix)
        
        # Aplicamos Gauss-Jordan a la matriz aumentada
        rref = augmented.gauss_jordan()
        
        # La inversa estará en las últimas columnas de la matriz RREF
        inverse_matrix = [rref[i][self.cols:] for i in range(self.rows)]
        return matrix(inverse_matrix)
    
m1 = matrix([[1,2], [3,4]])
m2 = matrix([[2,2], [2,2]])
m3 = m1 + m2
m4 = m1 - m2
m5 = m1 * 3
m6 = m1 * m2
print("\nMatriz 1: ")
print(m1)
print("\nMatriz 2: ")
print(m2)
print("\nMatriz 1 + Matriz 2: ")
print(m3)
print("\nMatriz Matriz 1 - Matriz 2: ")
print(m4)
print("\nMatriz 1 x 3: ")
print(m5)
print("\nMatriz 1 x Matriz 2: ")
print(m6)

#get item
print(m1[0])  
print(m1[2, 1]) #[filas, columnas]

# Modificar un elemento específico
m1[2, 0] = 5    #[filas, columnas]

# Modificar una fila completa
m1[2] = [5, 6]
print(m1) 

#potencias 
print("\nMatriz 2 ^2: ")
print(m2 ** 2)

#negativo
print("\nMatriz 1 (-1): ")
print(-m1)

#Valor absoluto:
print("\n|Matriz 1|: ")
print(abs(m1))

#eq:
print("\nMatriz 1 = Matriz 2 ? ")
print(m1 == m2)

#Inversa de una matriz
m1_inv = m1.inverse()
print("\nInversa de Matriz 1: ")
print(m1_inv)