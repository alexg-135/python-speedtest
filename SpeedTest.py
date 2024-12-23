import speedtest
import time
import os
import pygame
import pyttsx3
os.system('cls')
#----------------------------------------------------------------------------




#Definicije
os.system('mode con: cols=50 lines=1')


try:
    speedtest = speedtest.Speedtest()
except:
    os.startfile('NoInternetERROR.py')
    exit()

def clear():
    os.system('cls')
    
def AutoSTNow():
    print('???')



def ExitNow():
    Ponavljanje = 0
    remenskiRazmak = 0
    
with open('History.txt','r') as HistoryTXT:
    SavedHistory = HistoryTXT.read()
pygame.mixer.init()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#----------------------------------------------------------------------------


#Odabir opcija i Pokretanje
Ponavljanje = int(input('Koliko se puta treba poniviti: '))
clear()
if Ponavljanje != 1:
    if Ponavljanje != 0:
        VremenskiRazmak = float(input('Razmek između testiranja (Minute): '))*60
clear()

#---------------------------------------------------------------------------



#Učitavanje
ls = 0.1
os.system('mode con: cols=46 lines=43')
def Loading():
    os.system('mode con: cols=16 lines=7')
    print('\n\n\n       -')
    time.sleep(ls)
    clear()
    print('\n\n\n       \\')
    time.sleep(ls)
    clear()
    print('\n\n\n       |')
    time.sleep(ls)
    clear()
    print('\n\n\n       /')
    time.sleep(ls)
    clear()
    print('\n\n\n       -')
    time.sleep(ls)
    clear()
    print('\n\n\n       \\')
    time.sleep(ls)
    clear()
    print('\n\n\n       |')
    time.sleep(ls)
    clear()
    print('\n\n\n       /')
    time.sleep(ls)
    clear()
    print('\n\n\n       -')
    time.sleep(ls)
    clear()

if Ponavljanje != 0:
    Loading()
      
#----------------------------------------------------------------------------

#Učitavanje Povijesti
with open('History.txt','r') as HistoryTXT:
    SavedHistory = HistoryTXT.read()

#----------------------------------------------------------------------------



#Program

os.system('mode con: cols=46 lines=43')

if Ponavljanje == 1:
    VremenskiRazmak = 0
elif Ponavljanje == 0:
    os.startfile('MessageBoxPonavljanje0.py')
    with open('History.txt','w') as HistoryTXT:
        HistoryTXT.write(SavedHistory)
        HistoryTXT.write('\n')
        HistoryTXT.write('\n')
        HistoryTXT.write('\n')
        HistoryTXT.write('\n')
        HistoryTXT.write('\n>>> ERROR: Ponavljanje = 0 <<<')
    with open('History.txt','r') as HistoryTXT:
        SavedHistory = HistoryTXT.read()

    
    
print('##############################################')
with open('History.txt','w') as HistoryTXT:
    HistoryTXT.write(SavedHistory)
    HistoryTXT.write('\n')
    HistoryTXT.write('\n')
    HistoryTXT.write('\n>>> Novo Spremanje - ')
    HistoryTXT.write(time.ctime())
    HistoryTXT.write(' (Započeto)')
    HistoryTXT.write('\n########################################################')
    HistoryTXT.write('\n--------------------------------------------------------')
with open('History.txt','r') as HistoryTXT:
    SavedHistory = HistoryTXT.read()
with open('RedDownloadZone.txt','r')as rdzTXT:
    RedDownloadZone = int(rdzTXT.read())
with open('RedUploadZone.txt','r')as ruzTXT:
    RedUploadZone = int(ruzTXT.read())

for i in range(Ponavljanje):
    BrojP= str(i+1)+'.'
    DownSpeed = round((int(speedtest.download())*0.000001),2)
    UpSpeed = round((int(speedtest.upload())*0.000001),2)
    NowTime = time.ctime()
    
    print('----------------------------------------------')

    
    if DownSpeed<=RedDownloadZone:
        RedZoneWD ='!'
        pygame.mixer.music.load('MessageInfo.mp3')
        pygame.mixer.music.play()
        time.sleep(1)
    elif DownSpeed>=RedDownloadZone:
        RedZoneWD =' '
    if UpSpeed<=RedUploadZone:
        RedZoneWU='!'
        pygame.mixer.music.load('MessageInfo.mp3')
        pygame.mixer.music.play()
        time.sleep(1)
    elif UpSpeed>=RedUploadZone:
        RedZoneWU=' '

    if (DownSpeed <= RedDownloadZone)or(UpSpeed<=RedUploadZone):
        Say = 'Red Zone Warning.!'
        engine.say(Say)
        engine.runAndWait()
        if (float(DownSpeed) == 0) or (float(UpSpeed) == 0):
            Say = 'No internet connection.'
            engine.say(Say)
            engine.runAndWait()
        elif (DownSpeed < RedDownloadZone) and (UpSpeed<RedUploadZone):
            Say = 'Download speed is ' + str(DownSpeed) + ', and upload speed is ' + str(UpSpeed)
            engine.say(Say)
            engine.runAndWait()
        elif (DownSpeed<RedDownloadZone):
            Say = 'Download speed is ' + str(DownSpeed)
            engine.say(Say)
            engine.runAndWait()
        elif (UpSpeed<RedUploadZone):
            Say = 'Upload speed is ' + str(UpSpeed)
            engine.say(Say)
            engine.runAndWait()
        
        
    
    print('',BrojP,'Put  Vrijeme:',NowTime)
    print('')
    print('   ',str(RedZoneWD),' Download Speed: ',DownSpeed)
    print('   ',str(RedZoneWU),' Upload Speed:   ',UpSpeed)
    print('')
    os.system('color 07')
    print('----------------------------------------------')
    print('##############################################')

    with open('History.txt','w') as HistoryTXT:
        HistoryTXT.write(SavedHistory)
        HistoryTXT.write('\n ')
        HistoryTXT.write(str(BrojP))
        HistoryTXT.write(' Put   Vrijeme: ')
        HistoryTXT.write(NowTime)
        HistoryTXT.write('\n')
        HistoryTXT.write('\n')
        HistoryTXT.write('  ')
        HistoryTXT.write(RedZoneWD)
        HistoryTXT.write(' Download Speed: ')
        HistoryTXT.write(str(DownSpeed))
        HistoryTXT.write('\n')
        HistoryTXT.write('  ')
        HistoryTXT.write(str(RedZoneWU))
        HistoryTXT.write(' Upload Speed:   ')
        HistoryTXT.write(str(UpSpeed))
        HistoryTXT.write('\n')
        HistoryTXT.write('\n--------------------------------------------------------')
    with open('History.txt','r') as HistoryTXT:
        SavedHistory = HistoryTXT.read()
        
    time.sleep(VremenskiRazmak)

with open('History.txt','w') as HistoryTXT:
    HistoryTXT.write(SavedHistory)
    HistoryTXT.write('\n########################################################')
with open('History.txt','r') as HistoryTXT:
    SavedHistory = HistoryTXT.read()

#Gašenje

input('\nStisni enter za izlazak... ')
clear()

Loading()

os.system('mode con: cols=16 lines=3')
clear()
print('\n  Završeno ...')
time.sleep(2)
clear()
print('\n  Izlazak  ...')
time.sleep(2)
clear()
exit()

