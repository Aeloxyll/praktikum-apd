from tambahan import enter
from data import akun_user

def register(username, password):
    if username in akun_user:
        print(f"Akun '{username}' sudah terdaftar!")
    else:
        akun_user[username] = password
        print(f"Akun '{username}' berhasil ditambahkan!")
    enter()

def login_admin():
    username = input("Masukkan username admin: ")
    password = input("Masukkan password admin: ")
    if username == "admin" and password == "admin123":
        print("Login admin berhasil!")
        enter()
        return True
    else:
        print("Username atau password admin salah!")
        enter()
        return False

def login_user():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username in akun_user and password == akun_user[username]:
        print("Login user berhasil!")
        enter()
        return True
    else:
        print("Username atau password salah!")
        enter()
        return False
