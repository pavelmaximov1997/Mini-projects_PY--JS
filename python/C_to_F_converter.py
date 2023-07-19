temp = float(input("Enter the temperature: "))
unit = input("Celsius or Fahrenheit? (C/F): ")

if unit == "C":
    print(f"The temperature {temp} centigrade equals to", (temp * 1.8) + 32, "in Fahrenheit.")
elif unit == "F":
    print(f"The temperature {temp}F equals to", (temp - 32) / 1.8, "Centigrade.")
else:
    print("Please, enter something valid. You dumb arse flamingo.")
    