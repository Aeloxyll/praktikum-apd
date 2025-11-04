import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def enter():
    input("Tekan Enter untuk melanjutkan...")
