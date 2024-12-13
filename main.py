from user_input import User_input
from Budget_Percentage_Calculation import Budget
from continue_app import ask_to_continue

def main():
    while True:
        user = User_input(0, 0)
        user.get_user_input()

        result = Budget(user.income, user.fix_expenses)
        result.display_budget()

        if not ask_to_continue():
            break

if __name__ == "__main__":
    main()




