data = [5, 7, 9, 10, 14, 15]
 
n = len(data)
print(n)
mean = sum(data) / n
# Sum of squared differences from the mean
sq_diffs = [(x - mean) ** 2 for x in data]
 
# Population variance
population_variance = sum(sq_diffs) / n
 
# Sample variance
sample_variance = sum(sq_diffs) / (n - 1)
 
print("Manual Population Variance:", round(population_variance,2))
print("Manual Sample Variance:", sample_variance)
