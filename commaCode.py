def commaCode(lista):
    for item in lista:
        if(item == lista[len(lista)-1]):
            print(item, end = '.')
        elif(item == lista[len(lista)-2]):
            print(item, end = ' and ')
 
        else:
            print(item, end = ', ')
