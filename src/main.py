from utils import square, is_even, celsius_to_fahrenheit

number = float(input("Enter a number: "))

print(f"Square: {square(number)}")

if is_even(number):
    print(f"{number} is even")
else:
     print(f"{number} is odd")
print(f"Fahrenheit equivalent: {celsius_to_fahrenheit(number)}")
