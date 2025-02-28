# Budget_allocation_app

## Overview
 ###The Budget Allocation App is a command-line interface (CLI) tool designed to help users optimize their monthly income through tailored budgeting and expense planning. 
The app calculates how users can best allocate their income across various expense categories by allocating remaining income after fixed expense have been deducted. It provides a visual breakdown of spending into categories displaying in table format and in a pie chart in .png format.

## Features
    **User Input**: Collects monthly income and fixed expenses from the user.
    **Budget Allocation**: Calculates the budget and allocates for various categories such as Savings, Investments, Dining Out, and Guilt-Free Spending post     expenses deductions.
    **Budget Visualization**: Displays formated budgeted in tables and a pie chart representing the budget breakdown.

    *Supports multiple calculations
    *Includes error handling and input validation

## Requirement:
    Before running the app, ensure you have the following installed:
        - **Python 3.x** (Recommended: Python 3.8+)
        The following Python libraries (can be installed using 'pip'):
            - 'matplotlib': For visualizing the budget allocation in a pie chart.
            - 'tabulate': For formatting the budget data into a table.
            - 'colorama': For terminal text formatting (used to display colorful output).
            - 'pyfiglet': For printing the app header in an ASCII art style.

        You can install these dependencies by running:
           ```bash
            pip install matplotlib tabulate colorama pyfiglet```


## Installation
    ###Step 1: Create new folder for repository to be saved in.
    ```
    mkdir Budget_allocation_app
    cd Budget_allocation_app
    ```
    ### Step 2:
    Clone this repository to your local machine via terminal:
    ```
    git clone git@github.com:Angie-newbie/Budget_allocation_app.git
    ```

    ### Step 3:
    Create virtual environment to install dependencies in your IDE:
    
    ###Step 4: Install the required dependencies:
    ```
    pip install matplotlib tabulate colorama pyfiglet
    ```

    ###Step 3: Run the App
    ```
    python main.py
    ```

## Usage of app
In termimal:
```
python main.py
```
## Prompts
- Enter monthly income when prompted
- Enter fixed expenses when prompted
- Review budget allocation breakdown
- Choose to calculate another budget or exit

## Budget Allocations 
Savings: 25% of remaining income
Investments: 20% of remaining income
Emergency Fund: 15% of remaining income
Grocery: 15% of remaining income
Dining Out: 10% of remaining income
Transport: 5% of remaining income
Guilt-Free Spending: 10% of remaining income

## Output Format
- ASCII art header for visual engagement
- Formatted budget table using tabulate library
- Pie chart visualization saved as 'Budget_Allocation_Breakdown_PieChart.png'

## Error Handling
- Validates negative numbers
- Checks for invalid inputs
- Handles file operation errors
- Provides clear error messages

## Example of output
![output_example](https://github.com/user-attachments/assets/bdb3ea93-b49f-4fbf-ab08-c1f8a21c056c)


## Copyright and Licence 
    This project uses the following Python libraries:
    `matplotlib` (version 3.6.0) - Licensed under the [Matplotlib License](https://matplotlib.org/stable/users/license.html)
    - `tabulate` (version 0.9.0) - Licensed under the [MIT License](https://opensource.org/licenses/MIT)
    - `colorama` (version 0.4.6) - Licensed under the [MIT License](https://opensource.org/licenses/MIT)
    - `pyfiglet` (version 0.8) - Licensed under the [MIT License](https://opensource.org/licenses/MIT)
