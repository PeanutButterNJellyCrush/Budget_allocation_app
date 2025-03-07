# Import necessary modules
from user_input import User_input  # Imports the User_input class to handle user input
from Budget_Percentage_Calculation import (
    Budget,
)  # Imports the Budget class to perform budget calculations
from continue_app import (
    ask_to_continue,
)  # Imports the ask_to_continue function to check if the user wants another calculation
from colorama import Fore, Style
   # Imports colorama library
"""
The main function that runs the budget calculation program.
Workflow:
    1. Creates a "User_input" object with default values (0,0).
    2. Calls "get_user_input()" to collect income and fixed expenses.
    3. Creates a "Budget" object using the collected user data.
    4. Calls "display_budget()" to show the budget allocation.
    5. Calls "ask_to_continue()" to determine if the user wants to continue or exit.
    6. If "ask_to_continue()" returns False, the loop breaks, ending the program.
"""


def main():

    # Infinite loop to allow repeated budget calculations
    while True:

        # To ensure errors are handled
        try:

            # Create a User_input object with initial values (0 income, 0 fixed expenses)
            user = User_input(0, 0)

            # Prompt user for input (income & fixed expenses)
            user.get_user_input()

            # Create a Budget object using the user's input as "result"
            result = Budget(user.income, user.fix_expenses)

            # Display the calculated budget allocation
            result.display_budget()

            # Ask the user if they want to continue or exit
            if not ask_to_continue():
                # Exit the loop if user chooses 'n'
                break

        # Handle user exiting the app at any point with ctrl + c
        except KeyboardInterrupt:
            print(f"{Fore.YELLOW} command performed by user. This app has now terminated.{Style.RESET_ALL}")
            exit()

        # Handle unexpected errors
        except Exception as e:

            # Print an error message
            print(f"an unexpected error{e} occur")


# Ensures that the script runs only when executed directly, not when imported
if __name__ == "__main__":
    main()
