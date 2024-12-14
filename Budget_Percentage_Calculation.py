import matplotlib.pyplot as plt
from tabulate import tabulate
from colorama import Fore, Style, init
import pyfiglet

class Budget:
    def __init__(self, income, fixed_expenses):
        self.income = income
        self.fixed_expenses = fixed_expenses
        self.remaining_income = self.income - fixed_expenses

    def budget_calculation(self):
        calculate = lambda percantage: percantage * self.remaining_income
        savings = calculate(0.30)
        investments = calculate(0.20)
        dining_out = calculate(0.10) 
        guilt_free_spending = calculate(0.10)
        return savings, investments, dining_out, guilt_free_spending

    
    def display_budget(self):
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


    def print_header(self, font="small"):
        # Use pyfiglet to print the header in a cool ASCII art style
        header_style = pyfiglet.figlet_format("Budget App", font=font)
        print(Fore.CYAN + header_style)


    def display_budget_table(self, savings, investments, dining_out, guilt_free_spending):
        table = [
            ['Savings', f"${savings:.2f}"],
            ['Investments', f"${investments:.2f}"],
            ['Dining Out', f"${dining_out:.2f}"],
            ['Guilt-Free Spending', f"${guilt_free_spending:.2f}"]
        ]
        print(tabulate(table, headers=["Category", "Amount"], tablefmt="fancy_grid"))


    def pie_chart(self, savings, investments, dining_out, guilt_free_spending):
        categories = ['Savings', 'Investments', 'Dining Out', 'Guilt-Free Spending']
        values = [savings, investments, dining_out, guilt_free_spending]

        # function to format the labels with value 
        def func(pct, allvals): #pct: The percentage of the pie slice (how much of the total the slice represents).allvals: The list of all values (like values), which represents the total money in each category.
            absolute = round(pct / 100.*sum(allvals), 2)
            return f"${absolute:.2f}" 
        

        plt.pie(values, labels=categories, autopct=lambda pct: func(pct, values), startangle=140)
        plt.axis('equal')  # ensures that pie is drawn as a circle.
        plt.title("Budget Allocation Breakdown")
        plt.savefig("Budget_Allocation_Breakdown_PieChart")
        print("Pie chart has been saved as 'Budget_Allocation_Breakdown_PieChart.png'.")
        plt.close()


        