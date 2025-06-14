a = int(input("Enter a number: "))
b = []
sum = 0

while a > 0:
    digit = a % 10
    sum = sum + digit
    b.append(digit)  # Append the digit, not the sum
    a = a // 10

print("Sum of digits is", sum)
print("Digits in reverse order:", b)
for i in range(b):
    print(b[i], end=' ')