def comaFunction(lista):
    for i in range(len(lista)):
        if lista[len(lista)-2] == lista[i]:
            print(lista[i], end=" and ")
        elif lista[len(lista)-1] == lista[i]:
            print(lista[i], end= ".")
        else:
            print(lista[i], end=', ')


spam = ['apples', 'bananas', 'tofu', 'cats']


comaFunction(spam)
