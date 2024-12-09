## To Get User Input

class User_input:
    def __init__(self, income, fix_expenses):
        self.income = income
        self.fix_expenses = fix_expenses
    
    def get_user_input(self):
        try:
            self.income = float(input('Please enter your monthly income'))
            self.fix_expensess = float(input('Please enter your monthly fixed expenses'))
            return self.income, self.fix_expenses
        except ValueError:
            print(f'Error: Please enter a valid number')
    
