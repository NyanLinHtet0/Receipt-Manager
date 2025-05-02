#this function is a menu function
def menu(lst):
    if 'Exit' in lst:
        pass
    else:
        lst.append('Exit')
    print()
    i = 1
    for item in lst:
        print(str(i) + '. ' + item)
        i += 1
    while True:
        try:
            choice = int(input('Input: '))
            if 1 <= choice <= len(lst):
                print()
                return choice
            else:
                print('Invalid choice. Please enter a number between 1 and', len(lst))
        except ValueError:
            print('Invalid input. Please enter a valid number.')