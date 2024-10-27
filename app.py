'''
This code was created by SkyX
'''
from sistem.sistemKerja import*

bersihkan_terminal()
a = 1
while (a < 2):

    help_msg()
    masukan = input("shell > ")
    if masukan == "1":
        a = 1
        main()
        bersihkan_terminal()
    elif masukan == "2":
        a = 1
        help()
        bersihkan_terminal()
    elif masukan == "3":
        bersihkan_terminal()
        print("bye")
        break
    else:
        a = 1
        bersihkan_terminal()
