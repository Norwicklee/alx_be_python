monthly_income = float(input("Enter your monthly income:"))
monthly_expenses = float(input("Enter your total monthly expenses:"))

monthly_savings = monthly_income - monthly_expenses

Projected_Savings = ((monthly_savings * 12 * 1.05))

print(f"Your monthly savings are {monthly_savings}.")
print(f"Projected savings after one year, with interest, is {Projected_Savings}.")