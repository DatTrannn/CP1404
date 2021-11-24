import random

OUTPUT_FILE = 'capitalist_conrad.txt'  # the output file
MIN_PRICE = 0.01  # MINIMUM PRICE
MAX_PRICE = 1000  # MAXIMUM PRICE
day = 0
price = 10
out_file = open(OUTPUT_FILE, 'w')
while MIN_PRICE <= price <= MAX_PRICE:
    chance = random.randint(0, 1)
    # if chance == 0 --> price decrease
    # if chance == 1 --> price increase
    if day == 0:
        print(f"Starting price: ${price:.2f}", file=out_file)
    else:
        print(f"On day {day} price is: ${price:.2f}", file=out_file)
    if chance == 0:
        decrease_percent = random.uniform(0, 0.05)
        price -= price * decrease_percent
    else:
        increase_percent = random.uniform(0, 0.1)
        price += price * increase_percent
    day += 1

out_file.close()
