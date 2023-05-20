from playsound import playsound
import os

os.chdir('/home/darma/Music')
file = os.listdir()

while True :
    print('playlist music anda : ')
    for i in range(len(file)):
        print(f"{i}\t --> \t{file[i]}")
    try:
        i = int(input('masukkan playlist anda : '))
        print('Anda sedang memutar music {}'.format(file[i]))
        playsound(file[i])
    except:
        print('anda sudah keluar !')
        break



