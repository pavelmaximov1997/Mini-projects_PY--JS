principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input('Please, enter the principle amount in $: '))
    if principle <= 0:
        print("Invalid amount") 

while rate <= 0:
    rate = float(input('Please, enter the interest rate: %'))
    if rate <= 0:
        print("Invalid amount")

while time <= 0:
    time = int(input('Please, enter time in years: '))
    if time <= 0:
        print("Invalid amount")

total = principle * pow((1 + rate/100), time)
print(f"Your investment in {time} years will be ${total:,.2f}")