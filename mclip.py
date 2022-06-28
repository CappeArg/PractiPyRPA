#'''este será mi primer proyecto de python
#la verdad estoy nervioso y emocionado...
#emocionado por las posibilidades!!!
#y nervioso por lo mismo'''


TEXT = {'ok':'''Estoy de acuerdo''',
        'ocupado': '''Estoy complicado en este momento, leo y te escribo''',
        'recibido': '''Recibido, gracias por avisar'''}

import sys,pyperclip

if len(sys.argv)<2:
    print('Use python mclip.py[keyprhase] - copy phrase text')
    sys.exit()

keyphrase= sys.argv[1] #first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + 'copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)
