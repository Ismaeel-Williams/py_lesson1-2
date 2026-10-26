# Question 1: 
input_name = input("What is your name?")
input_age = input("What is your age?")
print("My name is " + input_name + " and I am " + input_age + " years old.")

# Question 2:
input_length = input("What is the length of the rectangle? ")
input_width = input("What is the width of the rectangle? ")
print("Area = " + str(float(input_length) * float(input_width)))

# Question 3:
input_temp = input("What is the temperature in Celsius? ")
converted_temp = (float(input_temp) * 9/5) + 32
print("Temp in Fahrenheit = " + str(round(converted_temp, 2)))