n = int(input("Enter the number of integers: "))
X = list(map(int, input("Enter the integers: ").split()))
F = list(map(int, input("Enter the frequency of each element: ").split()))

S = sorted(sum(([x]*y for x,y in zip(X, F)),[]), reverse=False)

total = len(S)
if total%2 != 0: odd = True
else: odd =False

total /= 2
total = int(total)
Lower = []
Upper = []

for i in range(0,total):
    Lower.append(S[i])

if odd:
    for i in range(total+1, len(S)):
        Upper.append(S[i])
else: 
    for i in range(total, len(S)):
        Upper.append(S[i])


########## defining function for median ##########
def median(integers, n):
    if n%2 != 0:
        q2 = integers[int(n/2)]
        return q2
    else: 
        q2 = (integers[int(n/2)]+integers[int(n/2)-1])/2
        return(q2)

Q1 = median(Lower, n=total)
Q3 = median(Upper, n=total)

print(float(Q3)-float(Q1))



