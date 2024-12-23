import time
import os

#Definicije
os.system('mode con: cols=50 lines=1')
def clear():
    os.system('cls')
#-------------------------------------------------------------------


#Pokretanje
os.system('mode con: cols=18 lines=3')
clear()
print('\n  Učitavanje ...')
time.sleep(3)

#program
os.system('mode con: cols=29 lines=9')
clear()
IzabranaOpcija = PovijestOpcija = ZonaOpcija = '0'


while IzabranaOpcija!='5':
    clear()
    print('>>>        IZABERI        <<<')
    print('>>>                       <<<')
    print('>>>  1) Testiraj Brzinu   <<<')
    print('>>>  2) Povijest          <<<')
    print('>>>  3) Update ipi        <<<')
    print('>>>  4) Crvena Zona       <<<')
    print('>>>  5) Izlaz             <<<')
    print('>>>                       <<<')
    IzabranaOpcija = input('>>> ')

    
    if IzabranaOpcija =='1':
        os.startfile('SpeedTest.py')

        
    elif IzabranaOpcija =='2':
        PovijestOpcija = '0'

        
        while PovijestOpcija!='5':
            clear()
            print('>>>  Povijest Testiranja  <<<')
            print('>>>                       <<<')
            print('>>>  1) Otvori TXT        <<<')
            print('>>>  2) Ispiši            <<<')
            print('>>>  3) Obriši            <<<')
            print('>>>  4) Spremi            <<<')
            print('>>>  5) Natrag            <<<')
            print('>>>                       <<<')
            PovijestOpcija = input('>>> ')
            if PovijestOpcija =='1':
                os.startfile('History.txt')

                
            elif PovijestOpcija =='2':
                os.startfile('HistoryReader.py')

            
            elif PovijestOpcija=='3':
                clear()
                os.startfile('HistoryReader.py')
                print('>>>  Povijest Testiranja  <<<')
                print('>>>  Brisanje  Povijesti  <<<')
                print('>>>                       <<<')
                print('>>>   jeste li sigurni?   <<<')
                print('>>>                       <<<')
                print('>>>      ( da / ne )      <<<')
                print('>>>                       <<<')
                print('>>>                       <<<')
                Brisanje = input('>>> ')
                if Brisanje=='da':
                    with open('History.txt','w') as HistoryTXT:
                        HistoryTXT.write('########################################################')
                        HistoryTXT.write('\n<<<<<<<<<<<<<<<<< Povijest  Testiranja >>>>>>>>>>>>>>>>>')
                        HistoryTXT.write('\n\n\n\n')


            elif PovijestOpcija=='4':










                SpremanjPovijestiOpcija = 0
                while SpremanjPovijestiOpcija != '3':
                    
                    try:
                        os.mkdir('SavedHistory')
                    except:
                        a=0
                    with open('SavedHistory\\Pročitaj Me.txt','w') as ProMeTXT:
                        ProMeTXT.write('\n########################################################')
                        ProMeTXT.write('\nU ovoj mapi ću vam biti sva spremanje koje napravite    ')
                        ProMeTXT.write('\n########################################################')
                    
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

                        print('>>>  Spremanje Povijesti  <<<')
                        print('>>>                       <<<')
                        print('>>>       Unesi Ime       <<<')
                        print('>>>                       <<<')
                        print('>>>                       <<<')
                        print('>>>          ...          <<<')
                        print('>>>                       <<<')
                        print('>>>                       <<<')
                        
                        SavedName = str(input('>>> '))
                        SavedName='SavedHistory\\' + SavedName +'.txt'
                        try:
                            with open(SavedName,'r') as Name:
                                test = Name.read()
                            Prolaz='false'
                            clear()
                            print('>>>  Spremanje Povijesti  <<<')
                            print('>>>                       <<<')
                            print('>>>    Unošeno ime  je    <<<')
                            print('>>>        zauzeto        <<<')
                            print('>>>                       <<<')
                            print('>>> Želiteli  zamijeniti? <<<')
                            print('>>>       (da / ne)       <<<')
                            print('>>>                       <<<')
                            Odluka = input('>>> ')
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















                


            elif PovijestOpcija=='5':
                PovijestOpcija='5'


            else:
                os.startfile('InputERROR.py')


    elif IzabranaOpcija =='3':
        os.startfile('Install or Update.py')
        exit()


    elif IzabranaOpcija =='4':
        ZonaOpcija = '0'


        while ZonaOpcija !='4':
            clear()
            print('>>>      Crvena Zona      <<<')
            print('>>>                       <<<')
            print('>>>  1) Donwload          <<<')
            print('>>>  2) Upload            <<<')
            print('>>>  3) Ugasi             <<<')
            print('>>>  4) Natrag            <<<')
            print('>>>                       <<<')
            print('>>>                       <<<')
            ZonaOpcija = input('>>>')


            if ZonaOpcija=='1':
                clear()
                print('>>>      Crvena Zona      <<<')
                print('>>>      Downloading      <<<')
                print('>>>                       <<<')
                print('>>>  Unesite minimalnu    <<<')
                print('>>>  brzinu, kada brzina  <<<')
                print('>>>  padne ispod          <<<')
                print('>>>  navedenog biti će    <<<')
                print('>>>  crvena               <<<')
                RedDownloadZoneInput = input('>>> ')
                with open('RedDownloadZone.txt','w') as RedDownloadZoneTXT:
                    RedDownloadZoneTXT.write(str(RedDownloadZoneInput))


            elif ZonaOpcija=='2':
                clear()
                print('>>>      Crvena Zona      <<<')
                print('>>>       Uploading       <<<')
                print('>>>                       <<<')
                print('>>>  Unesite minimalnu    <<<')
                print('>>>  brzinu, kada brzina  <<<')
                print('>>>  padne ispod          <<<')
                print('>>>  navedenog biti će    <<<')
                print('>>>  crvena               <<<')
                RedUploadZoneInput = input('>>> ')
                with open('RedUploadZone.txt','w') as RedUploadZoneTXT:
                    RedUploadZoneTXT.write(str(RedUploadZoneInput))


            elif ZonaOpcija=='3':
                clear()
                print('>>>      Crvena Zona      <<<')
                print('>>>        Gašenje        <<<')
                print('>>>                       <<<')
                print('>>>   jeste li sigurni?   <<<')
                print('>>>                       <<<')
                print('>>>      ( da / ne )      <<<')
                print('>>>                       <<<')
                print('>>>                       <<<')
                RedOffZoneInput = input('>>> ')


                if RedOffZoneInput=='da':
                    with open('RedUploadZone.txt','w') as RedUploadZoneTXT:
                        RedUploadZoneTXT.write('0')
                    with open('RedDownloadZone.txt','w') as RedDownloadZoneTXT:
                        RedDownloadZoneTXT.write(str('0'))


            elif ZonaOpcija=='4':
                ZonaOpcija = '4'


            else:
                os.startfile('InputERROR.py')
                
                      
    elif IzabranaOpcija=='5':
        IzabranaOpcija=='5'


    else:
        os.startfile('InputERROR.py')
