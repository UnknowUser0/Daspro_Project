from harga.harga import*
from tools.definisi import*
from tools.definisi import bersihkan_terminal

def main():
    bersihkan_terminal()
    nomor_receipt = receipt_no(nomor())
    i = 1
    while (i < 2):
        menu()

        bbm = 1
        while (bbm < 2):
            jenis_bbm = input("Masukan jesin bbm: ")
            bbm_upper = jenis_bbm.upper()
            if bbm_upper in ('1P', '2P', '3P', '4P'):
                bbm += 1
            else:
                print("Kode yang dimasukan salah")

        isi = 1
        while (isi < 2):
            pengisian = int(input("Masukan Harga pengisian: "))
            if pengisian < 10000:
                isi = 1
                print("Minimal pengisian Rp.10.000")
            else:
                isi += 1

        if bbm_upper == "1P":
            grade = "SUPER"
            volume = pengisian / shell_super
            unit_price = rupiah(shell_super)
            i = i + 1
        elif bbm_upper == "2P":
            grade = "V-POWER"
            volume = pengisian / shell_v_power
            unit_price = rupiah(shell_v_power)
            i = i + 1
        elif bbm_upper == "3P":
            grade = "NITRO+"
            volume = pengisian / shell_v_power_nitro
            unit_price = rupiah(shell_v_power_nitro)
            i = i + 1
        elif bbm_upper == "4P":
            grade = "V-POWER DIESEL"
            volume = pengisian / shell_v_power_diesel
            unit_price = rupiah(shell_v_power_diesel)
            i = i + 1
        else:
            i = 1
            print("Kode yang dimasukan salah")
            sleep(3)
            bersihkan_terminal()

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
    bersihkan_terminal()
    fuel_loading(volume, speed)
    simpan_ke_txt(struk(grade, volume, unit_price, pengisian,nomor_receipt),nomor_receipt)
    print(struk(grade, volume, unit_price, pengisian,nomor_receipt))

    input("enter to finish ")
    bersihkan_terminal()

def help():
    bersihkan_terminal()
    print('''
    jika ada masalah hubungi kami
    TELP.081218500112FAX
    WWW.SHELL.CO.ID/TELLSHELL
    ''')
    input()

