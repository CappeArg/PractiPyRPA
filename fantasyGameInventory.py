import pprint

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow':12}

def displayItems(dictionary):
    print('Items:')
    totalItems = 0

    for k,v in dictionary.items():
        totalItems += v
        pprint.pprint(k +': ' + str(v))

    print('Total number of items: ' + str(totalItems))

displayItems(stuff)
