import sys
import os

# Prompts the user to decide whether they want to calculate another budget
def ask_to_continue():

    """
    Infinite loop to keep asking until a valid response is received

    Returns:
    - `True`: If the user chooses to calculate another budget.
    - `False`: If the user chooses to exit the program.
    """
    while True:
        
        # To ensure errors are handled 
        try:

            # Ask user whether they want to calculate another budget and store the input as "answer"
            answer = input('Do you wish to calculate another budget? (y/n): ')

            # If user enters 'y', return True to continue the process
            if answer.lower() == 'y': 
                return True
    
            # If user enters 'n', print a message and return False to exit.
            elif answer.lower() == 'n':
                print('Thank you for using the Budget App!')
                return False
            
            # If the input is not 'y' or 'n', show an error message and prompt again.
            else:
                print("Invalid input! Please enter 'y' for yes or 'n' for no.")
                
        # Handle key interruption by user by pressing ctrl + c
        except KeyboardInterrupt:
            print(' command performed by user. This app has now terminated.')
            try:
                sys.exit()
            except SystemExit:
                os._exit(130)

        # Handle any unexpected errors
        except Exception as e :
            print(f'Error: Unexpected error {e} occor')
            