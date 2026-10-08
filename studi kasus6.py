# Sistem Manajemen Inventaris Barang

import json

path = r"C:\Users\User\OneDrive\PRATIKUM\StudiKasus6\inventaris1.json"

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)


def tambah_data(nama, stok, harga):
    data.append({
        "nama": nama,
        "stok": stok,
        "harga": harga
    })
    return "Data barang berhasil ditambahkan!"


def simpan_file():
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    return "Data berhasil disimpan ke inventaris_barang.json!"


while True:
    print("\n===== SISTEM MANAJEMEN INVENTARIS BARANG =====")
    print("1. Lihat Data Barang")
    print("2. Tambah Barang")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("\n--- DATA INVENTARIS BARANG ---")

        if len(data) == 0:
            print("Belum ada data barang.")
        else:
            for barang in data:
                print("Nama  :", barang["nama"])
                print("Stok  :", barang["stok"])
                print("Harga :", barang["harga"])
                print("-----------------------------")

    elif pilihan == "2":
        print("\n--- TAMBAH DATA BARANG ---")

        nama = input("Masukkan nama barang: ")
        stok = int(input("Masukkan stok barang: "))
        harga = int(input("Masukkan harga barang: "))

        print("\n", tambah_data(nama, stok, harga))
        print(simpan_file())

    elif pilihan == "3":
        print("\nProgram selesai.")
        break

    else:
        print("\nPilihan tidak tersedia.")