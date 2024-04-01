import math
print ("name keshav sahni rollno 2210997118 ")

numbers = [5, 10, 15, 20, 25]


mean = sum(numbers) / len(numbers)


variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)


std_deviation = math.sqrt(variance)


print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_deviation)
