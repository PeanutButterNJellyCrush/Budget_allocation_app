# A class to handle user input for income and fixed expenses.
class User_input:

    """
    Initializes the User_input object with income and fixed expenses.
    Parameters:
        - income (float): The user's monthly income (default is passed from main program).
        - fix_expenses (float): The user's monthly fixed expenses (default is passed from main program).
    """
    def __init__(self, income, fix_expenses):
        
        # Store the income value inside the object as self.income
        self.income = income

        # Store the fix_expense value inside the object as self.fix_expenses
        self.fix_expenses = fix_expenses
    
    """
    Prompts the user to enter their monthly income and fixed expenses.
        - Uses a loop to repeatedly ask for valid input until correct values are provided
        - Ensures that income is a positive number
        - Ensures that fixed expenses are non-negative
    """
    def get_user_input(self):
        
        # Create an infinite loop that the code inside will keep running until a valid input is received or an explicit break occurs
        while True:

            # Handle potential errors that may occur when taking user input.
            try:

                # Prompt user for monthly income and validate input
                self.income = float(input('Please enter your monthly income: '))

                # If the user input is negative
                if self.income <= 0:

                    # Print the error message
                    print(f"Error: Income cannot be zero or negative. Please enter a valid amount.")
                    
                    # Prompt again
                    continue

                # Prompt user for fixed expenses and validate input
                self.fix_expenses = float(input('Please enter your monthly fixed expenses: '))

                # If the user input is negative
                if self.fix_expenses < 0:

                    # Print the error message
                    print(f"Error: Expenses cannot be negative. Please enter a valid amount.")
                    
                    # Prompt again
                    continue

                # Return validated values for running the calculation
                return self.income, self.fix_expenses
                
            # Handles cases where the user enters a non-numeric value
            except ValueError:

                # Print the error message
                print(f'Error: Please enter a valid number')

                # Prompt again
                continue

            # Catches any other unexpected errors
            except Exception as e:
                # Print the error message
                print(f"Unexpected Error Occur {e}, Please double check your answer and try again :)")

                # Exits the function in case of an unexpected error
                return 

