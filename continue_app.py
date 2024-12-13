def ask_to_continue():
    answer = input('Do you wish to calculate another budget? (y/n): ')
    if answer != 'y':
        print('Thank you for using the Budget App!')
        return False
    else:
        return True