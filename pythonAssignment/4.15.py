import random

print ("name keshav sahni rollno 2210997118 ")
my_list = []
size = int(input("Enter the size of the list: "))


for i in range(size):
    my_list.append(random.randint(1, 100))


print("List before sorting:")
print(my_list)


my_list.sort()


print("List after sorting:")
print(my_list)
