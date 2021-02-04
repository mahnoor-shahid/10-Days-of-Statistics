
n = int(input("Enter number of integers: "))
integers = list(map(int, input("Enter the numbers: ").split()))

def average():
    sum = 0
    for i in range(0, n):
        sum += integers[i]
    return sum/n

def squared_distance():
    distance = 0
    values = []
    mean_value = average()
    for i in range(0, n):
        distance = integers[i]-mean_value
        distance = distance ** 2
        values.append(distance)
    return sum(values)

def standard_deviation():
    return round((squared_distance()/n) ** 0.5, 1)

print(standard_deviation()) 

