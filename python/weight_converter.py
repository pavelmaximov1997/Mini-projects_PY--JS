weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or P): ")
pound = 2.20462
if unit == "K":
    print("Your weight is:", weight, "kg")
    print("Or", weight * pound, "Lbs")
    
elif unit == "P":
    print("Your weight is:", weight, "Lbs")
    print("Or", weight / pound, "kg")
else:
    print(f"You can't weigh '{unit}', try again")
