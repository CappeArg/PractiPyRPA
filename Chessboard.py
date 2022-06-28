#Tablero de ejemplo
exampleBoard = {'1a': '', '2a': '', '3a': 'bKing', '4a': '', '5a': '', '6a': '', '7a': '', '8a': '', 
                '1b': '', '2b': '','3b': '', '4b': '', '5b': '', '6b': '', '7b': '', '8b': '', 
                '1c': '', '2c': '', '3c': '', '4c': '', '5c': '', '6c': '', '7c': '','8c': '', 
                '1d': '', '2d': '', '3d': '', '4d': '', '5d': '', '6d': '', '7d': '', '8d': '',
                '1e': '', '2e': '', '3e': '', '4e': '', '5e': '', '6e': '', '7e': '', '8e': '',
                '1f': '', '2f': '', '3f': '', '4f': '', '5f': '', '6f': '', '7f': '', '8f': '',
                '1g': '', '2g': '', '3g': '', '4g': '', '5g': '', '6g': '', '7g': '', '8g': '',
                '1h': '', '2h': '', '3h': '', '4h': '', '5h': '', '6h': '', '7h': '', '8h': '', } 

#Funcion para comprobar que los movimientos son correctos
def isValidChessBoard(board):
    
    valido = True #variable de respuesta

    #players=["b", "w"]
    spacesL =('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    names = {"pawn": 8, "knight": 2, "bishop": 2, "rook": 2, "queen": 1, "King": 1}
    spaces = []
    
    #Armo el tablero
    for lugar in spacesL:
        contador = 1
        while contador <= 8:
            spaces.append(str(contador) + lugar)
            contador+=1
 
#Listas con los lugares y piezas del tablero            
    lugares = []
    piezas = []
    
#Relleno los lugares y las piezas en el tablero, en dos listas separadas
    for space, pieces in board.items():
        lugares.append(space)
        piezas.append(pieces)


#Controlo un rey de cada jugador
    bk = 0
    wk = 0 
    for pieza in piezas:
        if (pieza) == "":
            continue
        else:
            if pieza[0] == "b":
                if pieza[1:] == "":
                    bk+=1
            elif pieza[0] == "w":
                if pieza == "w" +  names[5]:
                    wk+=1
    #Respuesta por el rey:
    if bk > 1 or bk < 1 or wk > 1 or wk < 1:
        valido=False

        

    
    print("Rey Blanco: " + str(wk))
    print("Rey Negro: " + str(bk))
    print(valido)
    print(lugares)


    
isValidChessBoard(exampleBoard)


        
