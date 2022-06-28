cats = []

while True:
    print('Enter the name of cat ' + str(len(cats) + 1) +
          ' (Or enter nothig to stop.): ')
    name = input()
    if name == '':
        break
    cats = cats + [name] #list concatenation
print('The cat names are; ')
for name in cats:
    print(' ' + name)
