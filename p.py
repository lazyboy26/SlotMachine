import random
import time

buah = ['🥭', '🍎', '🍊', '🥑', '💣', '🍌', '🥭', '🍎', '🍊', '🍌']

Random = None
Random1 = None
Random2 = None
saldo = 1000
bet = None

print("Halo Selamat Datang Di Game Slot")


def play():
    global Random, Random1, Random2, Random3, Random4, saldo, asking
    asking = askPlayer()
    spin()


def spin():
    global Random, Random1, Random2, Random3, Random4, saldo, asking
    while(saldo != 0 and asking == True):
        Random = hitung()
        Random1 = hitung()
        Random2 = hitung()
        Random3 = hitung()
        Random4 = hitung()
        print()
        time.sleep(1)
        Score()
        time.sleep(.5)
        print()
        asking = askPlayer()


def askPlayer():
    '''
    Asks the player if he wants to play again.
    expecting from the user to answer with yes, y, no or n
    No case sensitivity in the answer. yes, YeS, y, y, nO . . . all works
    '''
    global saldo
    while(True):
        jawab = input("Saldo Untuk Bermain Adalah $" +
                      str(saldo) + ". Apakah Kamu Ingin Bermain? ")
        jawab = jawab.lower()
        if(jawab == "yes" or jawab == "y"):
            return True
        elif(jawab == "no" or jawab == "n"):
            print("Kamu Mengakhiri Permainan Dengan Membawa Pulang Uang $" + str(saldo))
            return False
        else:
            print("INPUT SALAH")


def hitung():
    Random = random.sample(buah, 6)
    return Random


def Score():
    global Random, Random1, Random2, Random3, Random4, saldo

    print(str(Random))
    print(Random1)
    print(Random2)
    print(Random3)
    print(Random4)

    hasil = Random + Random1 + Random2 + Random3 + Random4

    hitungApple = hasil.count('🍎')
    hitungPisang = hasil.count('🍌')
    hitungMangga = hasil.count('🥭')
    hitungJeruk = hasil.count('🍊')
    hitungAvocado = hasil.count('🥑')
    hitungScater = hasil.count('💣')

    print("🍎", hitungApple)
    print("🍌", hitungPisang)
    print("🥭", hitungMangga)
    print("🍊", hitungJeruk)
    print("🥑", hitungAvocado)
    print("💣", hitungScater)

    if hitungApple >= 8:
        win = 25
        saldo += win
        print("🍎", hitungApple, " Apple!! Selamat Kamu Mendapatkan $ ", win, " 🍎")
    elif hitungPisang >= 8:
        win = 5
        print("🍌", hitungPisang, " Pisang!! Selamat Kamu Menang ", win, ' 🍌')
    elif hitungMangga >= 8:
        win = 15
        print("🥭", hitungMangga, " Mangga!! Selamat Kamu Menang", win, ' 🥭')
    elif hitungJeruk >= 8:
        win = 10
        print("🍊", hitungJeruk, " Jeruk!! Selamat Kamu Menang", win, ' 🍊')
    elif hitungAvocado >= 8:
        win = 30
        print("🥑", hitungAvocado, " Avocado!! Selamat Kamu Menang", win, ' 🥑')
    elif hitungScater >= 4:
        win = 50
        saldo += win
        print("💥 BOOM!!Selamat Kamu Menang JACKPOT 💥")
        spin()
    else:
        win = -10

    saldo += win
    if win > 0:
        print("Ini Hari Keberuntunganmu")
    else:
        print("Maaf, Mungkin Lain Kali")


play()
