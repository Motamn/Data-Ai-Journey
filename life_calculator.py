repeat = "yes"
while repeat.lower() == "yes":
  name = input("Enter Name: ")
  age = int(input("Enter Age: "))
  exp_age = int(input("Enter Expected Age: "))

  if age > exp_age:
    print("You lived more than you expected!!")
  else:
    
    rem_age = exp_age - age 
    print(f"{name} you have {rem_age} years remaining!")
    rem_age_days = rem_age * 365
    print(f"and that's will be {rem_age_days} days...")
    repeat = input("Do you want to repeat (yes/no): ")