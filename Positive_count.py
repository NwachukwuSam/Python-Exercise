count = 0
positiveNumbers = 0
negativeNumbers = 0
number = int(input("Enter a Number: "))
total = 0
average = 0
positive_count=0
negative_count=0
while number != 0:
    if number > 0:
        positive_count+= 1
        positiveNumbers = positiveNumbers + number
    if number < 0:
        negative_count+=1
        negativeNumbers = negativeNumbers + number
    number = int(input("Enter a Number: "))
    count += 1
    total = positiveNumbers + negativeNumbers
    average = total / count
print("Sum of Positive integers =", positiveNumbers)
print("Sum of Negative integers =", negativeNumbers)
print("Sum of Numbers inputed =", total)
print("Average of Numbers inputed =", average)
print("Number of Negative Integers =", negative_count)
print("NUmber of Positive Integers =", positive_count)