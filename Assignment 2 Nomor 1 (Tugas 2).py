#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Daftar_Kontak():
    print("Nama : Tata")
    print("No. Telepon : 88989918")
    print("Nama : Baba")
    print("No. Telepon : 99898819")

def Tambah_Kontak():
    Nama = str(input("Nama Anda: "))
    No = int(input("No. Telepon: "))
    
def Keluar():
    print("Terima Kasih")

def show_menu():
    print ("\nSelamat Datang")
    print ("-----------------")
    print ("1) Daftar Kontak ")
    print ("2) Tambah Kontak")
    print ("3) Keluar")
    
def menu():
    while True:
        show_menu()
        choice = input('Pilih menu: ').lower()
        if choice == '1':
            Daftar_Kontak()
        elif choice == '2':
            Tambah_Kontak()
        elif choice == '3':
            Keluar()
        else:
            print(f': <{choice}>, Tidak ada dalam pilihan menu')

if __name__ == '__main__':
    menu()
    


# In[ ]:




