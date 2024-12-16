try:
    import matplotlib.pyplot as plt
    from tabulate import tabulate
    from colorama import Fore, Style, init
    import pyfiglet
except ImportError as e:
    print(f'Error: The package {e.name} is not installed. Please install it by running: pip install {e.name}')
    exit(1)

class Budget:
    def __init__(self, income, fixed_expenses):
        self.income = income
        self.fixed_expenses = fixed_expenses
        self.remaining_income = self.income - fixed_expenses
        if income is None or fixed_expenses is None:
            return
        if self.remaining_income <= 0:
           raise ValueError("{Fore.RED}Expenses cannot be larger than income, or equal to the income{Style.RESET_ALL}")

    def budget_calculation(self):
        calculate = lambda percantage: percantage * self.remaining_income
        savings = calculate(0.30)
        investments = calculate(0.20)
        dining_out = calculate(0.10) 
        guilt_free_spending = calculate(0.10)
        return savings, investments, dining_out, guilt_free_spending

    
    def display_budget(self):
        try: 
            savings, investments, dining_out, guilt_free_spending = self.budget_calculation()
            self.print_header("small")
            print(f"{Fore.RED}Your Monthly Budget Allocation:")
            catergories = [
                            ("Saving" , savings), 
                            ("Investment" , investments), 
                            ("Dining-out" , dining_out),
                            ("Guilt Free Spending" , guilt_free_spending)
                        ]
            for category, value in catergories:
                print(f"{Fore.BLUE}{category}:{Style.RESET_ALL} ${value:.2f}")
            self.display_budget_table(savings, investments, dining_out, guilt_free_spending)
            self.pie_chart(savings, investments, dining_out, guilt_free_spending)
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


    def display_budget_table(self, savings, investments, dining_out, guilt_free_spending):
        try: 
            table = [
                ['Savings', f"${savings:.2f}"],
                ['Investments', f"${investments:.2f}"],
                ['Dining Out', f"${dining_out:.2f}"],
                ['Guilt-Free Spending', f"${guilt_free_spending:.2f}"]
            ]
            print(tabulate(table, headers=["Category", "Amount"], tablefmt="fancy_grid"))
        except Exception as e:
            print(f"Error: Unable to display the budget table. {e}")



    def pie_chart(self, savings, investments, dining_out, guilt_free_spending):
        categories = ['Savings', 'Investments', 'Dining Out', 'Guilt-Free Spending']
        values = [savings, investments, dining_out, guilt_free_spending]

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