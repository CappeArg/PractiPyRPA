def spam():
    global eggs
    eggs = 'spam'

eggs = 'GLOBAL'
spam()
print(eggs)
