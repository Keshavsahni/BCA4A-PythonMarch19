print ("name keshav sahni rollno 2210997118 ")
def is_pos_neg_or_zero(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
num = float(input("Enter a number: "))
print("The number is", is_pos_neg_or_zero(num))
