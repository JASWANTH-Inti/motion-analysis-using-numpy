# motion-analysis-using-numpy
A Python project which uses NumPy to analyze velocity &amp; time data and predict the acceleration of a moving cart using basic physics and array operations.

Motion Analysis Using NumPy

Physics Formula used:

For motion with constant acceleration and zero initial velocity:

v = a × t

Therefore,

a = v / t

Where:
v = velocity (m/s)
t = time (s)
a = acceleration (m/s²)

Steps Performed:

1. Velocity & time data reading from a CSV file using NumPy.
2. Time and velocity are stored as NumPy arrays.
3. Acceleration is calculated using vectorized operations.
4. Mean and standard deviation of acceleration were calculated.
5. Performed difference between NumPy views and copies.
6. Created a 2D matrix and computed its transpose.
7. Saved time, velocity and acceleration data to a new CSV file.

Final Result:

Estimated acceleration = 2.03 m/s²
