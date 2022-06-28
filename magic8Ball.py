import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'Es cierto'
    elif answerNumber == 2:
        return 'Es decididamente así'
    elif answerNumber == 3:
        return 'Sí'
    elif answerNumber == 4:
        return 'Respuesta nebulosa, intente nuevamente'
    elif answerNumber == 5:
        return 'Pregunte nuevamente más tarde'
    elif answerNumber == 6:
        return 'Concentrese y pregunte nuevamente'
    elif answerNumber == 7:
        return 'Mi respuesta es No'
    elif answerNumber == 8:
        return 'Panorama no muy bueno'
    elif answerNumber == 9:
        return 'Muy dudoso'

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)
    
