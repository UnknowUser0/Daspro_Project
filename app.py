import os
from random import*
from time import sleep
import datetime

from harga.harga import*
from penghitung.hitung import*

no = 0
while (1 == 1):
    no += 1
    tanggal = datetime.datetime.now()
    pump_id1 = randint(1,10)
    pump_id2 = randint(1,10)
    i = 1

    while (i < 2):
        print('''
        +======================================================+
        |                  ____  _          _ _                |
        |                 / ___|| |__   ___| | |               |
        |                 \___ \| '_ \ / _ \ | |               |
        |                  ___) | | | |  __/ | |               |
        |                 |____/|_| |_|\___|_|_|               |
        +======================================================+
        +======================================================+
        |Shell Super           (1P)  | Rp. 12.290              |
        |Shell V-Power         (2P)  | Rp. 13.070              |
        |Shell V-Power Nitro+  (3P)  | Rp. 13.260              |
        |Shell V-Power Diesel  (4P)  | Rp. 13.250              |
        +======================================================+
        ''')
        jenis_bbm = input("Masukan jesin bbm: ")
        pengisian = int(input("Masukan Harga pengisian: "))

        if jenis_bbm.upper() == "1P" :
            grade = "SUPER"
            volume = pengisian / shell_super
            unit_price = "12290"
            i = i + 1
        elif jenis_bbm.upper() == "2P" :
            grade = "SUPER"
            volume = pengisian / shell_v_power
            unit_price = "12290"
            i = i + 1
        elif jenis_bbm.upper() == "3P" :
            grade = "SUPER"
            volume = pengisian / shell_super
            unit_price = "12290"
            i = i + 1
        elif jenis_bbm.upper() == "4P" :
            grade = "SUPER"
            volume = pengisian / shell_super
            unit_price = "12290"
            i = i + 1
        else:
            i = 1
            print("Kode yang dimasukan salah")
            sleep(3)
            os.system('clear')

        l = 1
        speed = 0
        while (l < 2):
            speed_pengisian = int(input("Speed pengisian 1-3: "))
            if speed_pengisian == 1:
                speed = 0.3
                l = l + 1
            elif speed_pengisian == 2:
                speed = 0.6
                l = l + 1
            elif speed_pengisian == 3:
                speed = 1
                l = l + 1
            else:
                i = 1
                print("speed yang dimasukan salah")

    sleep(1)
    os.system('clear')
    fuel_loading(volume, speed)

    print(f"""
        SHELL METLAND
    JL.CYBER CITY METLAND
    CV.ARYA SEJAHTERA ID 12484726
    NPWP.41.286.865.5_416.000
    TELP.081218500112FAX.
    PUMP ID {pump_id1}_{pump_id2}
    
    {tanggal.day}/{tanggal.month}/{tanggal.year}                 {str(tanggal.hour)[:2]}:{str(tanggal.minute)[:2]}
    Receipt No. :{no}
    
    Pump No.                {str(pump_id2).rjust(8)}
    Grade                   {grade.rjust(8)}
    Volume                  {str(volume)[:4].rjust(8)}
    Unit Price(Rp.)         {str(unit_price).rjust(8)}
    Amount(Rp.)             {str(pengisian).rjust(8)}
    
    TERIMAKASIH ATAS KUNJUNGAN ANDA
    HARGA SUDAH TERMASUK PAJAK
    WWW.SHELL.CO.ID/TELLSHELL
    """)


    looping = input("> ")
    if looping.upper() == "QUIT" or looping.upper() == "Q":
        break
    elif looping.upper() == "HELP" or looping.upper() == "H":
        os.system("clear")
        i = 1
        while (i < 2):
            print('''
            help (h) - help
            quit (q) - to exit
            enter to back
            ''')
            inputlop = input("> ")
            if inputlop.upper() == "HELP" or inputlop.upper() == "H":
                os.system("clear")
                i = 1

            elif inputlop.upper() == "QUIT" or inputlop.upper() == "Q":
                i = i + 2
                os.system("clear")
                break
            else:
                i = i + 3
                os.system("clear")
                break
        if i == 4:
            continue
        else:
            break
            os.system('clear')
    else:
        continue
    os.system('clear')
