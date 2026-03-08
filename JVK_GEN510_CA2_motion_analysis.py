import numpy as np

# Part A: CSV File Input & Arrays

data = np.genfromtxt('velocity_data.csv', delimiter=',', skip_header=1)

t = data[:,0]                                       # t in sec
v = data[:,1]                                       # v in m/s

print("Time:", t)
print("Velocity:", v)

print("\nArray Attributes")
print("Dimensions:", t.ndim)
print("Shape:", t.shape)
print("Size:", t.size)
print("Data Type:", t.dtype)


# Part B: Mathematical & Statistical Operations
# vectorized acceleration calculation

a = v / t

print("\nAcceleration values:", a)                   # a in m/s^2

mean_acc = np.mean(a)
std_acc = np.std(a)

print("Mean acceleration:", mean_acc)
print("Standard deviation:", std_acc)

print("\nEstimated acceleration = {:.3g} m/s^2".format(mean_acc))


# Part C: Copy vs View Demonstration

print("\n--- View Example ---")

slice_view = a[0:3]
slice_view[0] = 100

print("Modified slice:", slice_view)
print("Original array after modifying slice:", a)

print("\n--- Copy Example ---")

a = v / t  # reset acceleration

slice_copy = a[0:3].copy()
slice_copy[0] = 200

print("Modified copy:", slice_copy)
print("Original array after modifying copy:", a)


# Part D: Two Dimensional Matrix Ops

ones = np.ones(len(t))

matrix = np.column_stack((t, ones))

print("\nMatrix:")
print(matrix)

print("Matrix Shape:", matrix.shape)

print("Matrix Transpose:")
print(matrix.T)


# Part E: Save Results to New CSV File

results = np.column_stack((t, v, a))

np.savetxt(
    "acceleration_results.csv",
    results,
    delimiter=",",
    header="t,v,a",
    comments=""
)

print("\nResults saved to acceleration_results.csv")