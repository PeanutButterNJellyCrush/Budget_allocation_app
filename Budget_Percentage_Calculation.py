# Import necessary libraries, handling missing packages errors
try:
    # Import matplotlib.pyplot to generate a pie chart visualization of the budget as "plt"
    import matplotlib.pyplot as plt 

    # Import tabulate to display budget breakdown in a table format
    from tabulate import tabulate 

    # To add coloured text in console output
        # Fore: For changing the text colour (e.g., Fore.RED for red text)
        # Style: For additional text formatting like BRIGHT, DIM, and NORMAL
        # init: To ensure compatibility with Windows terminals by enabling ANSI color codes
    from colorama import Fore, Style, init 

    # Import pyfiglet for ASCII art title formatting
    import pyfiglet 

# Handling the case where an imported package is missing
except ImportError as e:
    # Prints an error message specifying the missing package, with {e.name} which contains the name of the package that failed to import
    print(f'Error: The package {e.name} is not installed. Please install it by running: pip install {e.name}')
    # Exits the program to ensure that the script does not continue running, and preventing runtime error
    exit(1)

# A class to represents a monthly budget allocation system
class Budget:
    # Initializes the budget with income and expenses, ensuring values are valid.
    # Parameters:
        # income (float): The user's total monthly income.
        # fixed_expenses (float): The total fixed expenses deducted from the income.
    def __init__(self, income, fixed_expenses):
        # Attributes:
        # income (float): Stores the provided income value.
        self.income = income

        # fixed_expenses (float): Stores the provided fixed expenses value.
        self.fixed_expenses = fixed_expenses

        # remaining_income (float): Calculates the disposable income by subtracting fixed expenses from income.
        self.remaining_income = self.income - fixed_expenses

        # Ensuring income and expenses are provided
        if income is None or fixed_expenses is None:
            # Avoids further calculations with missing data
            return
        
        # Validate that expenses are not equal to or greater than income
        if self.remaining_income <= 0:
            #raise an error message is displayed in red, preventing incorrect budgeting, and reset the colours
           raise ValueError("{Fore.RED}Expenses cannot be larger than income, or equal to the income{Style.RESET_ALL}")

    #  Calculates budget allocation based on fixed percentage categories.
    def budget_calculation(self):

        # Define a lambda function called 'calculate' that takes a percentage and calculates that percentage of the remaining income (self.remaining_income)
        calculate = lambda percantage: percantage * self.remaining_income

        # Calculate each category of the budget using the lambda function
        savings = calculate(0.25)            # 25% of remaining income is for savings
        investments = calculate(0.20)        # 20% of remaining income is for investments
        dining_out = calculate(0.10)         # 10% of remaining income is for dining out
        grocery = calculate(0.15)            # 15% of remaining income is for groceries
        transport = calculate(0.05)          # 5% of remaining income is for transport
        guilt_free_spending = calculate(0.10) # 10% of remaining income is for guilt-free spending
        emergency_fund = calculate(0.15)     # 15% of remaining income is for the emergency fund

        # Return all the calculated budget categories as a tuple
        return savings, investments, dining_out, grocery, guilt_free_spending, emergency_fund, transport

    # Displaying the user's monthly budget allocation
    def display_budget(self):

        # Attempt to execute the budget display logic
        try: 

            # Get the budget categories and their values by calling the budget_calculation method
            savings, investments, dining_out, grocery, guilt_free_spending, emergency_fund, transport = self.budget_calculation()

            # Print a small header to introduce the budget display
            self.print_header("small")

            # Print the text in red text 
            print(f"{Fore.RED}Your Monthly Budget Allocation:")

            # Define a list of tuples containing budget categories and their calculated values
            # Each tuple consists of two elements: the category name (as a string) and the corresponding value
# that was calculated earlier in the budget_calculation() method.
            catergories = [
                            ("Saving" , savings), 
                            ("Investment" , investments), 
                            ("Dining-out" , dining_out),
                            ("Grocery", grocery),
                            ("Transport", transport),
                            ("Guilt Free Spending" , guilt_free_spending),
                            ("Emergency Fund", emergency_fund)
                        ]
            
            # Loop through each category and its corresponding value, printing them in blue text, with the value in two decimal places with reseted colour
            for category, value in catergories:
                print(f"{Fore.BLUE}{category}:{Style.RESET_ALL} ${value:.2f}")
            
            # Call the method "display_budget_table" to display the budget in a table format
            self.display_budget_table(savings, investments, dining_out, grocery, guilt_free_spending, emergency_fund, transport)

            # Call the method "pie_chart" to display a pie chart representing the budget allocation visually
            self.pie_chart(savings, investments, dining_out, grocery, guilt_free_spending, emergency_fund, transport)

            # In case of any error, print an error message in red, and reset the text style after this
        except Exception as e:
            print(f"{Fore.RED}Error in displaying the budget: {e}{Style.RESET_ALL}")



    def print_header(self, font="small"):
        # Use pyfiglet to print the header in a cool ASCII art style
        try: 
            header_style = pyfiglet.figlet_format("Budget App", font=font)
            print(Fore.CYAN + header_style)
        except FileNotFoundError:
            print(f"{Fore.RED}Error: The specified font '{font}' was not found. Using default font.{Style.RESET_ALL}")
            font = "standard"
            header_style = pyfiglet.figlet_format("Budget App", font=font)
            print(Fore.CYAN + header_style)
        except Exception as e:
            print(f'{Fore.RED}An unexpected error occurred while generating the header: {e}{Style.RESET_ALL}')
        except UnicodeEncodeError as e:
            print(f"{Fore.RED}Error: Failed to print the header due to encoding issues: {e}{Style.RESET_ALL}")


    def display_budget_table(self, savings, investments, dining_out, grocery, guilt_free_spending, emergency_fund, transport):
        try: 
            table = [
                ['Savings', f"${savings:.2f}"],
                ['Investments', f"${investments:.2f}"],
                ['Dining Out', f"${dining_out:.2f}"],
                ['Grocery', f"${grocery:.2f}"],
                ['Transport', f"${transport:.2f}"],
                ['Guilt-Free Spending', f"${guilt_free_spending:.2f}"],
                ['Emergency Fund', f"${emergency_fund:.2f}"]
            ]
            print(tabulate(table, headers=["Category", "Amount"], tablefmt="fancy_grid"))
        except Exception as e:
            print(f"Error: Unable to display the budget table. {e}")



    def pie_chart(self, savings, investments, dining_out, grocery, guilt_free_spending, emergency_fund, transport):
        categories = ['Savings', 'Investments', 'Dining Out', 'Grocery', 'Transport', 'Guilt-Free Spending', 'Emergency Fund']
        values = [savings, investments, dining_out, grocery, guilt_free_spending, emergency_fund, transport]

        # function to format the labels with value 
        def func(pct, allvals): #pct: The percentage of the pie slice (how much of the total the slice represents).allvals: The list of all values (like values), which represents the total money in each category.
            absolute = round(pct / 100.*sum(allvals), 2)
            return f"${absolute:.2f}" 
        
        try:
            plt.pie(values, labels=categories, autopct=lambda pct: func(pct, values), startangle=140)
            plt.axis('equal')  # ensures that pie is drawn as a circle.
            plt.title("Budget Allocation Breakdown")
            plt.savefig("Budget_Allocation_Breakdown_PieChart")
            print("Pie chart has been saved as 'Budget_Allocation_Breakdown_PieChart.png'.")
            plt.close()
        except FileNotFoundError as e:
            print(f"Error: Could not save the file. {e}")
        except Exception as e:
            print(f"Error: Unable to generate the pie chart. {e}")