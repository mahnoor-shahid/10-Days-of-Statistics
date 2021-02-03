
n = int(input("Enter number of integers: "))
numbers = list(map(int,(input("Enter numbers: ").split())))
weights = list(map(int, input("Enter their respective weights: ").split()))

weighted_sum = 0
for i in range(0, n):
    weighted_sum += numbers[i] * weights[i]
output = weighted_sum/sum(weights)

print(round(output,1))