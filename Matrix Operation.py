import numpy as np

# 設定矩陣
matrix_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# 矩陣加法
matrix_add = np.add(matrix_a, matrix_b)

# 矩陣減法
matrix_subtract = np.subtract(matrix_a, matrix_b)

# 矩陣乘法
matrix_multiply = np.dot(matrix_a, matrix_b)

# 矩陣轉置
matrix_transpose = np.transpose(matrix_a)

# 輸出結果
print("矩陣 A:")
print(matrix_a)
print("\n矩陣 B:")
print(matrix_b)
print("\n矩陣加法結果:")
print(matrix_add)
print("\n矩陣減法結果:")
print(matrix_subtract)
print("\n矩陣乘法結果:")
print(matrix_multiply)
print("\n矩陣轉置結果:")
print(matrix_transpose)