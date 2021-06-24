balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12.0
# prevBalance = balance
for i in range(12):
    balance = balance * (1 - monthlyPaymentRate) * (monthlyInterestRate + 1)
    # IMHO, keeping these makes understanding the code easier
    # minMonthlyPayment = monthlyPaymentRate * prevBalance
    # monthlyUnpaidBalance = prevBalance - minMonthlyPayment
    # newBalance = monthlyUnpaidBalance * (monthlyInterestRate + 1)
    # prevBalance = newBalance

balance = round(balance, 2)
print(f"Remaining balance: {balance}")
