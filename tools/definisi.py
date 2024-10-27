import os
import sys
from time import*
from random import*
import datetime

def rupiah(duit):
    a = str(duit)
    if len(a) <= 3:
        return a
    else:
        b = a[:-3]
        c = a[-3:]
        return rupiah(b) + "." + c

'''
def loading(value):
    time = value / 0.20
    for i in range(int(time)):
        a = "--------------------"
        load = a.replace("-" ,"#" , i)
        print(f"Sedang mengisi ({load})")
        sleep(1)
        i = i + 1
        os.system('clear')
'''


def fuel_loading(total_liters, speed):
    duration = total_liters / speed  # Menentukan durasi total proses
    bar_length = 30  # Panjang bar untuk progres visual
    refresh_rate = 0.02  # Interval pembaruan dalam detik (50 ms)
    steps = int(duration / refresh_rate)  # Total langkah agar sesuai dengan durasi
    liters_per_step = total_liters / steps  # Liter bertambah per langkah

    print("Pengisian BBM dimulai...")
    print(f"Total Liter: {total_liters:.2f}L")

    for i in range(steps + 1):
        # Menghitung liter yang sudah terisi
        current_liters = min(liters_per_step * i, total_liters)  # Hindari melebihi total
        percentage = (current_liters / total_liters) * 100
        filled_length = int(bar_length * (current_liters / total_liters))

        # Membuat tampilan bar progres
        bar = "#" * filled_length + "-" * (bar_length - filled_length)

        # Menampilkan bar dengan liter yang terisi dan persentase
        sys.stdout.write(f"\r[{bar}] {current_liters:.2f}L / {total_liters:.2f}L | {percentage:.2f}%")
        sys.stdout.flush()

        # Tunggu sejenak sebelum lanjut ke langkah berikutnya
        sleep(refresh_rate)

    print("\nPengisian selesai.")
    sleep(3)
    bersihkan_terminal()

def bersihkan_terminal():
    command ='clear'
    if os.name in ('nt','dos'):
        command = 'cls'
    os.system(command)

def menu():
    print('''
    +======================================================+
    |                ____  _          _ _                  |
    |               / ___|| |__   ___| | |                 |
    |               \___ \| '_ \ / _ \ | |                 |
    |                ___) | | | |  __/ | |                 |
    |               |____/|_| |_|\___|_|_|                 |
    +======================================================+
    +======================================================+
    |Shell Super           (1P)  | Rp. 12.290              |
    |Shell V-Power         (2P)  | Rp. 13.070              |
    |Shell V-Power Nitro+  (3P)  | Rp. 13.260              |
    |Shell V-Power Diesel  (4P)  | Rp. 13.250              |
    |Pengisian minimal Rp. 10.000                          |
    +======================================================+
    ''')

def receipt_no(no):
    a = str(no)
    b = "000000"
    c = len(a)
    hasil = b[:(6 - c)] + a
    return hasil

def nomor():
    global no
    try:
        no += 1
    except:
        no = 1
    return no

def help_msg():
    print('''
    Selamat Datang di Shell
    
    1. pengisian
    2. bantuan
    3. keluar
        ''')

def struk(grade,volume,unit_price,pengisian,nomor_receipt):
    tanggal = datetime.datetime.now()
    pump_id1 = randint(1, 9)
    pump_id2 = randint(1, 9)
    spasiGRADE = " " * (27 - len(grade))
    spasiVol = " " * (26 - len(str(volume)[:4]))
    spasiPrice = " " * (17 - len(str(unit_price)))
    spasiAmount = " " * (21 - len(str(pengisian)))

    text = f"""
    +======================================+
    |       SHELL METLAND                  |
    |   JL.CYBER CITY METLAND              |
    |   CV.ARYA SEJAHTERA ID 12484726      |
    |   NPWP.41.286.865.5_416.000          |
    |   TELP.081218500112FAX.              |
    |   PUMP ID {pump_id1}_{pump_id2}                        |
    |                                      |
    |   {tanggal.strftime("%d")}/{tanggal.strftime("%m")}/{tanggal.year}                 {str(tanggal.strftime("%H"))}:{str(tanggal.strftime("%M"))}   |
    |   Receipt No. :{nomor_receipt}                |
    |                                      |
    |   Pump No.                       {str(pump_id2)}   |
    |   Grade{spasiGRADE}{grade}   |
    |   Volume{spasiVol}{str(volume)[:4]}   |
    |   Unit Price(Rp.){spasiPrice}{str(unit_price)}   |
    |   Amount(Rp.){spasiAmount}{str(pengisian)}   |
    |                                      |
    |   TERIMAKASIH ATAS KUNJUNGAN ANDA    |
    |   HARGA SUDAH TERMASUK PAJAK         |
    |   WWW.SHELL.CO.ID/TELLSHELL          |
    |                                      |
    +======================================+
    """
    return text

def simpan_ke_txt(text,nomor_receipt):
    file = open(f'struk/struk-{nomor_receipt}', 'w')
    file.write(text)