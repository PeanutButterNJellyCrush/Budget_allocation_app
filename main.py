from user_input import User_input
from Budget_Percentage_Calculation import Budget

user = User_input(0, 0)
user.get_user_input()

result = Budget(user.income, user.fix_expenses)
result.display_budget()
