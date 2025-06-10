import os
import time

def logout (login):
    print('\n')
    print('Efetuando logout...')
    login.clear()
    time.sleep(1.75)
    os.system('cls' if os.name == 'nt' else 'clear')