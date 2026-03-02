#1
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
total = np.sum(arr)
print("Array:", arr)
print("Sum of all elements:", total)
print()

#2
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])
print("Array:\n", arr)

# Sum of rows
print("Row-wise sum:", np.sum(arr, axis=1))

# Sum of columns
print("Column-wise sum:", np.sum(arr, axis=0))

# 2nd Maximum Element
flat = arr.flatten()
flat_sorted = np.sort(flat)
second_max = flat_sorted[-2]
print("Second Maximum Element:", second_max)
print()

#3
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
result = np.dot(A, B)
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Matrix Multiplication:\n", result)
print()

#4
import pandas as pd
data = {'X':[78,85,96,80,86],
        'Y':[84,94,89,83,86],
        'Z':[86,97,96,72,83]}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Element-wise power (X^Y example)
power_df = df ** 2
print("\nSquared DataFrame:\n", power_df)
#result = df['X'] ** df['Y']
#print(result)
print()

#5
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
             'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9,
              20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2,
                 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no',
                'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a','b','c','d','e','f','g','h','i','j']
df = pd.DataFrame(exam_data, index=labels)
print("First three rows of the data frame:")
print(df.head(3))

#6
data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Marks': [90, np.nan, 75, np.nan]
}
df = pd.DataFrame(data)
print("Before replacing:\n", df)

# Replace NaN with 0 (or mean)
df['Marks'].fillna(df['Marks'].mean(), inplace=True)
print("\nAfter replacing:\n", df)

#7
data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Marks': [90, np.nan, 75, np.nan]
}
df = pd.DataFrame(data)
print("Before replacing:\n", df)

# Replace NaN with 0 (or mean)
df['Marks'].fillna(df['Marks'].mean(), inplace=True)
print("\nAfter replacing:\n", df)