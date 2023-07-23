products = []
prices = []
total = 0
counter = 0
while True:
    product = input('Add a purchase(q to quit): ')
    if product.lower() == 'q':
        print('Thanks for shopping with us!')
        break
    else:
        price = float(input(f'What is the price of {product}?: $'))
        products.append(product)
        prices.append(price)      

print('___ YOUR RECEIPT ___')
for product in products:
    counter += 1
    print(product)
print()
for price in prices:
        total += price
print(f'You have purchased {counter} products')
print(f'Your total is ${total}')
print('See you again!')
