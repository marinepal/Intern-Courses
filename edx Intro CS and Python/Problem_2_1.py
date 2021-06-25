balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


def remainingBalance(balance: int, annualInterestRate: float, monthlyPaymentRate: float) -> float:
    monthlyInterestRate = annualInterestRate / 12.0
    # prevBalance = balance
    for i in range(12):
        balance = balance * (1 - monthlyPaymentRate) * (monthlyInterestRate + 1)
        # IMHO, keeping these makes understanding the code easier
        # minMonthlyPayment = monthlyPaymentRate * prevBalance
        # monthlyUnpaidBalance = prevBalance - minMonthlyPayment
        # newBalance = monthlyUnpaidBalance * (monthlyInterestRate + 1)
        # prevBalance = newBalance

    return round(balance, 2)


def remainingBalanceRecursive(balance: int, annualInterestRate: float, monthlyPaymentRate: float,
                              monthsLeft=12) -> float:
    monthlyInterestRate = annualInterestRate / 12.0
    balance = balance * (1 - monthlyPaymentRate) * (monthlyInterestRate + 1)
    if monthsLeft == 1:
        return round(balance, 2)
    return remainingBalanceRecursive(balance, annualInterestRate, monthlyPaymentRate, monthsLeft - 1)


print(f"Remaining balance: {remainingBalance(balance, annualInterestRate, monthlyPaymentRate)}")
print(f"Remaining balance: {remainingBalanceRecursive(balance, annualInterestRate, monthlyPaymentRate)}")
