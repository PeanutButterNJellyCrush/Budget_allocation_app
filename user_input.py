## To Get User Input

class User_input:
    def __init__(self, income, fix_expenses):
        self.income = income
        self.fix_expenses = fix_expenses
    
    def get_user_input(self):
        while True:
            try:
                self.income = float(input('Please enter your monthly income: '))
                if self.income <= 0:
                    print(f"Error: Income cannot be zero or negative. Please enter a valid amount.")
                    continue
                self.fix_expenses = float(input('Please enter your monthly fixed expenses: '))
                if self.fix_expenses < 0:
                    print(f"Error: Expenses cannot be negative. Please enter a valid amount.")
                    continue
                return self.income, self.fix_expenses
                
                
            except ValueError:
                print(f'Error: Please enter a valid number')
                continue
            except Exception as e:
                print(f"Unexpected Error Occur {e}, Please double check your answer and try again :)")
                return 

