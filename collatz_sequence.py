def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    
    print(result)
    return result

try:
    print('Please Enter a Number:')
    user_num = int(input())
    
    while user_num != 1:
        user_num = collatz(user_num)
        
except ValueError:
    print('Error: Please enter an real integer!')
