from Audio_to_string.funcoes import *

intro()
while True:
    fala = reconhecimento()
    print(f'Você disse: {fala}\n')
    fala_jarvieees(fala)
