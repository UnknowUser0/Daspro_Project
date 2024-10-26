import os
import sys
from time import*
from tqdm import tqdm


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
    refresh_rate = 0.025  # Interval pembaruan dalam detik (50 ms)
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
    os.system('clear')
