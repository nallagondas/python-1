#1. Install Jupyter notebook and run the first program and share the screenshot of the output.

print("Hello World! , Welcome to Python!")

x = 10
y = 10

# printing the type of the variables
print(type(x))
print(type(y))
# printing the value of the variables
print(x)
print(y)
# printing the reference ( id ) of both variables
print(id(x))
print(id(y))

# changing the value of variable y
y = 25
# printing the reference ( id ) of both variables again
print(id(x))
print(id(y))