# Import necessary libraries, handling missing packages errors
try:
    """
    To add coloured text in console output
        Fore: For changing the text colour (e.g., Fore.RED for red text)
        Style: For additional text formatting like BRIGHT, DIM, and NORMAL
        init: To ensure compatibility with Windows terminals by enabling ANSI color codes
    """
    from colorama import Fore, Style

# Handling the case where the colorama package is missing
except ImportError as e:
    # Prints an error message specifying the missing package
    print(f"Error: The package {e.name} is not installed. Please install it by running: pip install {e.name}")
    # Exits the program to ensure that the script does not continue running, and prevents runtime errors
    exit(1)

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

                    # Print the error message in red
                    print(f"{Fore.RED}Error: Income cannot be zero or negative. Please enter a valid amount.{Style.RESET_ALL}")
                    
                    # Prompt again
                    continue

                # Prompt user for fixed expenses and validate input
                self.fix_expenses = float(input('Please enter your monthly fixed expenses: '))

                # If the user input is negative
                if self.fix_expenses < 0:

                    # Print the error message in red
                    print(f"{Fore.RED}Error: Expenses cannot be negative. Please enter a valid amount.{Style.RESET_ALL}")
                    
                    # Prompt again
                    continue

                # # If the user expesnes > monthly income: 
                if self.fix_expenses > self.income:
                    print(f"{Fore.RED}Error: Expenses cannot be greater than your monthly income. Please try again.{Style.RESET_ALL}")
                    
                    #Prompt again
                    continue

                # Return validated values for running the calculation
                return self.income, self.fix_expenses
            
                
            # Handles cases where the user enters a non-numeric value
            except ValueError:

                # Print the error message in red
                print(f"{Fore.RED}Error: Please enter a valid number{Style.RESET_ALL}")

                # Prompt again
                continue

            # Catches user pressing ctrl + c
            except KeyboardInterrupt:
                 
                #  Print the message in yellow
                 print(f"{Fore.YELLOW}App exited by user.{Style.RESET_ALL}")

                #  exit the app
                 exit()

            # Catches any other unexpected errors
            except Exception as e:
                # Print the error message
                print(f"{Fore.RED}Unexpected Error Occurred: {e}, Please double check your answer and try again.{Style.RESET_ALL}")

                # Exits the function in case of an unexpected error
                return 

