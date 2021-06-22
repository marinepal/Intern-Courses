balance, annualInterestRate = 88, 0.2

monthlyInterestRate = annualInterestRate / 12.0
fixedMonthlyPayment, tempBalance = 0, balance
while tempBalance > 0:
    fixedMonthlyPayment += 10
    tempBalance = balance
    for i in range(12):
        tempBalance = (tempBalance - fixedMonthlyPayment) * (monthlyInterestRate + 1)

print("Lowest Payment:", fixedMonthlyPayment)
