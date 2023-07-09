import numpy
import threading
class MatrixMultiplication:
    def __init__(self):
        self.dimension1=input('Enter the dimension of matrix 1:')
        self.dimension2=input('Enter the dimension of matrix 2:')
    def matrix1(self):
        self.number_row_m1=self.dimension1.split()[0]
        self.number_column_m1=self.dimension1.split()[1]
        return [[float(input(f'Enter number for {i + 1} column and {j + 1} row for matrix 1:')) for i in range(int(self.number_column_m1))] for j in range(int(self.number_row_m1))]
    def matrix2(self):
        self.number_row_m2=self.dimension2.split()[0]
        self.number_column_m2=self.dimension2.split()[1]
        return [[float(input(f'Enter number for {i + 1} column and {j + 1} row for matrix 2:')) for i in range(int(self.number_column_m2))] for j in range(int(self.number_row_m2))]
    def dot(self):
        if int(self.dimension1.split()[1])==int(self.dimension2.split()[0]):
            m1 = self.matrix1()
            print('Matrix 1 is:')
            print(m1)
            m2 = self.matrix2()
            print('Matrix 2 is:')
            print(m2)
            print('The matrix product is:')
            print(numpy.dot(m1, m2))
        else:
            print('Multiplication is not possible!')
matrix_multiplication=MatrixMultiplication()
t1=threading.Thread(target=matrix_multiplication.dot)
t1.start()