import numpy as np

# Array creation
a = np.array([1, 2, 3])
b = np.arange(10)
c = np.linspace(0, 1, 5)
d = np.zeros((2, 3))
e = np.ones((3, 2))
f = np.eye(3)
g = np.random.rand(2, 3)
print("Array creation:")
print(a, b, c, d, e, f, g, sep="\n")

# Indexing and slicing
print("\nIndexing and slicing:")
print("b[2:5]:", b[2:5])
print("g[1, :]:", g[1, :])

# Math operations
print("\nMath operations:")
print("a + 10:", a + 10)
print("a * 2:", a * 2)
print("np.exp(a):", np.exp(a))
print("np.sqrt(a):", np.sqrt(a))

# Broadcasting
print("\nBroadcasting:")
print("a + np.array([10]):", a + np.array([10]))

# Reshaping and stacking
h = np.arange(6).reshape(2, 3)
i = np.vstack([h, h])
j = np.hstack([h, h])
print("\nReshaping and stacking:")
print("h:\n", h)
print("vstack:\n", i)
print("hstack:\n", j)

# Aggregation
print("\nAggregation:")
print("Sum:", h.sum())
print("Mean:", h.mean())
print("Max:", h.max())
print("Axis 0 sum:", h.sum(axis=0))
print("Axis 1 sum:", h.sum(axis=1))

# Random
print("\nRandom:")
print("randint:", np.random.randint(0, 10, (2, 3)))
print("normal:", np.random.normal(0, 1, (2, 3)))

# Linear algebra
k = np.array([[1, 2], [3, 4]])
l = np.array([[2, 0], [1, 2]])
print("\nLinear algebra:")
print("Dot:", np.dot(k, l))
print("Transpose:\n", k.T)
print("Inverse:\n", np.linalg.inv(k))
print("Eigenvalues:", np.linalg.eigvals(k))

# Masking and boolean indexing
print("\nMasking and boolean indexing:")
mask = a > 1
print("a > 1:", a[mask])

# Save and load
np.save('array.npy', a)
a_loaded = np.load('array.npy')
print("\nSaved and loaded array:", a_loaded)
