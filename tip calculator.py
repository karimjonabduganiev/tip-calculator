print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage to tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people  to split the bill? "))

tip_procent = tip / 100
bill_procent = bill * tip_procent
bill_total = bill + bill_procent
total = bill_total / people

final = round(total, 2)
final = "{:.2f}".format(total)

print(f"Each person should pay: ${final}")
