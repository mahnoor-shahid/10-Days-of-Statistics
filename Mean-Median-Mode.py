import numpy as np
from scipy import stats

n = int(input("Enter the total number of integers: "))

numbers = list(map(int, input().split()))

print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))