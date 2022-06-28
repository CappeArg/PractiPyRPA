import sys

while True:
    print('Type exit to to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print ('You typed ' + response + '.')
