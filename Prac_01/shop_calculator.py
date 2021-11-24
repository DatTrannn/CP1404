items_num = int(input('Number of items: '))
total = 0
while items_num < 0:
    print("Invalid number of items!")
    items_num = int(input('Number of items: '))
for i in range(items_num):
    price = float(input('Price of item: '))
    total += price

if total > 100:
    total -= total * 0.1
print(f"Total price for {items_num} items is ${total:.2f}")
