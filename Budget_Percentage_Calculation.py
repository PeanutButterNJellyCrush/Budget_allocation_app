class Budget:
    def __init__(self, income, fixed_expenses):
        self.income = income
        self.fixed_expenses = fixed_expenses
        self.remaining_income = self.income - fixed_expenses

    def budget_calculation(self):
        savings = self.remaining_income * 0.30 
        investments = self.remaining_income * 0.20
        dining_out = self.remaining_income * 0.10  
        guilt_free_spending = self.remaining_income * 0.10
        return savings, investments, dining_out, guilt_free_spending
    
    def display_budget(self):
        savings, investments, dining_out, guilt_free_spending = self.budget_calculation()
        print(f"Your Monthly Budget Allocation: Saving: {savings}, Investment: {investments}, Dining-put : {dining_out}, Guilt Free Spending{guilt_free_spending}")