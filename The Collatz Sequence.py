def collatz(number):
#even
    if (number % 2 == 0):
        result = number / 2
        return result
#odd        
    else:
        result =  3 * number + 1
        return result
try:
    usernumber = int(input("Input a number"))
    while usernumber !=1:
        print(collatz(usernumber))
        usernumber = collatz(usernumber)

except: print("ingrese un numero entero y dejese de joder")


