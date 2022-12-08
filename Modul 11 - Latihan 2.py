# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 18:06:23 2022

@author: Audi Aulia
"""

class Student:
    
    def __init__(self, nama, nilai):
        self.nama = nama
        self.__nilai = nilai
        
    @property
    def detail(self):
        return "Nama : {} \nNilai : {}".format(self.nama, self.__nilai)
    
    @property
    def nilai(self):
        pass
    
    @nilai.getter
    def nilai(self):
        return self.__nilai
    
    @nilai.setter
    def nilai(self, input):
        self.__nilai = input
        
    @nilai.deleter
    def nilai(self):
        self.__nilai = None
        
def banner():
    print("===== Program OOP =====")
    print("1. Mendeklarasikan Objek")
    print("2. Menampilkan Objek")
    print("3. Merubah Nilai Objek")
    print("4. Menghapus Objek") 
    print("5. Keluar Dari Program\n")
banner()
        
def main():
    student = Student(None, None)
    F = False
    while(not F):
        choice = int(input("Masukkan Pilihan Berupa Angka (1/2/3/4/5) : "))
        if(choice == 1):
            nama = input("Masukkan Namamu : ")
            nilai = int(input("Masukkan Nilaimu :"))
            student = Student(nama, nilai)
            print("Data Berhasil Ditambahkan")
            print("\n")
        elif(choice == 2):
            print("\n")
            print(student.detail)
            print("\n")
        elif(choice == 3):
            option = input("Apa yang ingin diubah (Nama/Nilai) : ").upper()
            if(option == "NAMA"):
                nama = input("Masukkan Nama : ")
                student.nama = nama
                print("Data Nama Berhasil Dirubah")
                print("\n")
            elif(option == "NILAI"):
                nilai = int(input("Masukkan Nilai : "))
                student.nilai = nilai
                print("Data Nilai Berhasil Dirubah")
                print("\n")
            else:
                print("Masukkan Kembali Opsi Anda (Nama/Nilai)")
                print("\n")
        elif(choice == 4):
            student.nilai = None
            del student.nilai
            print("Data Berhasil Dihapus")
            print("\n")
        elif(choice == 5):
            print("Terima Kasih Sudah Menggunakan Program Saya")
            F = True
        else:
            print("Masukkan Angka Sesuai Dengan Yang Ada di Menu!")
            print("\n")
main()