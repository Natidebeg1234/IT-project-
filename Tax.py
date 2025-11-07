def calculate_tax(income):
    if income <= 2000:
        tax_rate = 0
    elif income <= 4000:
        tax_rate = 0.15
    elif income <= 7000:
        tax_rate = 0.20
    elif income <= 10000:
        tax_rate = 0.25
    elif income <= 14000:
        tax_rate = 0.30
    else:
        tax_rate = 0.35

    tax_owed = income * tax_rate
    net_income = income - tax_owed

    return tax_owed, net_income

income = float(input("Enter your income: "))
tax, net = calculate_tax(income)

print("Tax Owed: $", round(tax, 2))
print("Net Income: $", round(net, 2))
