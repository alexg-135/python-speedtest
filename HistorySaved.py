import os
import time
def clear():
    os.system('cls')

os.system('mode con: cols=29 lines=9')
SpremanjPovijestiOpcija = 0
while SpremanjPovijestiOpcija != '3':
    clear()
    print('>>>  Spremanje Povijesti  <<<')
    print('>>>                       <<<')
    print('>>>                       <<<')
    print('>>>  1) Otvori Mjest      <<<')
    print('>>>  2) Novo              <<<')
    print('>>>  3) Natrag            <<<')
    print('>>>                       <<<')
    print('>>>                       <<<')
    SpremanjPovijestiOpcija = input('>>> ')

    if SpremanjPovijestiOpcija =='1':
        os.startfile('SavedHistory')


    elif SpremanjPovijestiOpcija =='2':
        with open('History.txt','r') as HistoryTXT:
            SavedHistory = HistoryTXT.read()
        clear()
        SavedName = str(input('Unesite Ime Spremanje: '))
        SavedName='SavedHistory\\' + SavedName +'.txt'
        try:
            with open(SavedName,'r') as Name:
                test = Name.read()
            Prolaz='false'
            clear()
            print('To ime je već zauzeto')
            Odluka = input('Želiteli zamijeniti(da/ne):')
            if Odluka=='da':
                Prolaz='true'
            elif Odluka=='ne':
                Prolaz='false'
            else:
                os.startfile('InputERROR.py')
        except:
            Prolaz='true'
            
        if Prolaz=='true':
            with open(SavedName,'w') as Name:
                Name.write(SavedHistory)

        


    elif SpremanjPovijestiOpcija =='3':
        SpremanjPovijestiOpcija = '3'


    else:
        os.startfile('InputERROR.py')
