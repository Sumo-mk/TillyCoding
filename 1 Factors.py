Factors = ""
Count = 1
x = int(input("Please enter a number"))
for i in range(100):
    Y = x % Count 
    if Y == 0:
        Factors += str(Count)
        Factors += ","
    Count = Count + 1
print(Factors)