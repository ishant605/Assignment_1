first_number = float(input("Enter a first number: "))
second_number = float(input("Enter a second number: "))

add = first_number + second_number
sub = first_number - second_number
mul = first_number * second_number
if second_number != 0:
    div = first_number / second_number
else:
    div = 0

print("Addition: ", add)
print("Subtraction: ", sub)
print("Multiplication: ", mul)
print("Division: ", div)