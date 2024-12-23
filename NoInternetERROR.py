import time
import os
import speedtest
os.system('mode con: cols=33 lines=5')

print('                                 ')
print('   Niste Povezani s internetom   ')
print('   Ne možemo pokrenuti program   ')
print('   Povežite se s internetom...   ')

time.sleep(5)
Prolaz=0
while Prolaz==0:
    try:
       speedtest = speedtest.Speedtest()
       os.system('cls')
       print('                                 ')
       print('           Povezano...           ')
       print('                                 ')
       print('                                 ')
       time.sleep(2)
       os.startfile('SpeedTest.py')
       Prolaz=1
    except:
        os.system('cls')
        print('                                 ')
        print('   Povežite se s internetom...   ')
        print('                                 ')
        print('                                 ')
        time.sleep(5)
exit()
