#task was - allow input of 3 numbers and compare them 
Sum = 0
High = 0
Low = 100
List = 1
Num = 0
Avg = 0
Max = 0
Mini = 0


List = int(input("How many numbers do you wish to input?"))
print(List)
for x in range(List):                                  #allows for more than 3 inputs
    Num = int(input("Please enter the number"))
    if Num > High:
        High = Num
        Max = Num

    if Num < Low:
        Low = Num
        Mini = Num

    Sum = Num + Sum

Avg = Sum / List
print("The maximum was ",Max )
print("The minimum was ", Mini)
print("The sum was ", Sum, ". The average was ", Avg)