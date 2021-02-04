
n = int(input("Enter the number of integers: "))
integers = sorted(list(map(int, input("Enter the integers: ").split())), reverse=False)

########## defining function for median ##########
def median(integers, n):
    if n%2 != 0:
        q2 = integers[int(n/2)]
        return q2
    else: 
        q2 = (integers[int(n/2)]+integers[int(n/2)-1])/2
        if q2%1==0: return (int(q2))
        else: return(q2)


########## quartile 2 ##########
q2 = median(integers, n)


########## building lower and upper groups ##########
if n%2 != 0: include= True
else: include= False
n /=2
n = int(n)
Lower = []
Upper = []
for i in range(0, n):
    Lower.append(integers[i])
if include:
    for i in range(n+1,len(integers)):
        Upper.append(integers[i])
else: 
    for i in range(n,len(integers)):
        Upper.append(integers[i])


########## quartile 1 ##########
q1 = median(integers=Lower, n=n)

########## quartile 3 ##########
q3 = median(integers=Upper, n=n)

print(q1)
print(q2)
print(q3)