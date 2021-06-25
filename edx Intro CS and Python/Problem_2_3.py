balance, annualInterestRate = 3392, 0.2
monthlyInterestRate = annualInterestRate / 12.0
low, high = round(balance / 12.0, 3), round(balance * (1 + monthlyInterestRate) ** 12 / 12.0, 3)
tempBalance = balance
while True:
    fixedMonthlyPayment = round((low + high) / 2.0, 3)
    tempBalance = balance
    for i in range(12):
        tempBalance = (tempBalance - fixedMonthlyPayment) * (monthlyInterestRate + 1)
    if 0 >= tempBalance >= -0.12:
        break
    elif tempBalance > 0:
        low = fixedMonthlyPayment
    elif tempBalance < 0:
        high = fixedMonthlyPayment

print(f"Lowest Payment: {round(fixedMonthlyPayment, 2)}")
