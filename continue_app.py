def ask_to_continue():
    while True:
        try:
            answer = input('Do you wish to calculate another budget? (y/n): ')
            if answer == 'y':
                return True
            elif answer == 'n':
                print('Thank you for using the Budget App!')
                return False
            else:
                print("Invalid input! Please enter 'y' for yes or 'n' for no.")
        except Exception as e :
             print(f'Error: Unexpected error {e} occor')
            