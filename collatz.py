def collatz(number):
    
    while number != 1:
        if number % 2 == 0:
            number = number /2
            print(number)
        else:
            number = number * 3 + 1
            print(number)
                

try:
    collatz(int(input('Please, enter a number:  ')))

except ValueError:
    print('It must be a integer number')
