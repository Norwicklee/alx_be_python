monthly_income = float(input("Enter your monthly income:"))
monthly_expenses = float(input("Enter your total monthly expenses:"))

monthly_savings = int(monthly_income - monthly_expenses)

Projected_Savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print(f"Your monthly savings are {monthly_savings}.")
print(f"Projected savings after one year, with interest, is {Projected_Savings}.")