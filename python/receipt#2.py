products = {}
total = 0
max_length = int(input('How many items are you going to buy?: '))

while len(products) < max_length:
    item = input("Add a purchase: ")
    price = float(input(f"And price of the {item}: $"))

    products[item] = price

print()

print('___ YOUR RECEIPT ___')
for key, value in products.items():
    total += value
    print(f'{key}     :     ${value}')

print()
print('____________________')
print(f'Your total is ${total}')
print('See you again!')