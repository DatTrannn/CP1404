TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff = (input("Which tariff? 11 or 31: "))
if tariff == 11:
    price = TARIFF_11
else:
    price = TARIFF_31
usage = float(input("Enter daily use in kWh: "))
bills_per_day = int(input("Enter number of billing days: "))
total = price * usage * bills_per_day
print(f"Estimated bill: ${total:.2f}")
