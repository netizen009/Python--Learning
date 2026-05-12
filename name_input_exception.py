try:
    print('Enter your name:')
    name = input().strip() # Cleaning the spaces
    
    if name == '':
        raise Exception('Error: Name section must include at least one character')
    else:
        print(f'Hello, {name}!')

except Exception as err:
    print(f'An Error occured: {err}')
