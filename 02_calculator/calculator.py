def add(x,y):
  return x + y

def sub(x,y):
  return x - y

def multi(x,y):
  return x * y

def div(x,y):
  if y == 0:
    return "Error: Cannot divide by zero!"
  else:
    return x / y

def mod(x,y):
  return x % y

repeat = "yes"
while repeat.lower() == "yes":
  print("Choose operation: +, -, *, /, %")
  operation = input("Operation: ").strip()
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))

  if operation == "+":
    result = add(num1,num2)
  elif operation == "-":
    result = sub(num1,num2)
  elif operation == "*":
    result = multi(num1,num2)
  elif operation == "/":
    result = div(num1,num2)
  elif operation == "%":
    result = mod(num1,num2)
  else:
    result= f"The Opeartion \"{operation}\" is invalid"

  print(f"Result: {result}")
  repeat = input("Do you want to calculate again? (yes/no): ")


