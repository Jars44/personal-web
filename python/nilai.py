def check_nilai():
    while True:
        nilai = input("Masukkan nilai (atau ketik 'exit' untuk keluar): ")
        
        if nilai.lower() == 'exit':
            print("Terima kasih! Program dihentikan.")
            break
        
        try:
            nilai = int(nilai)
            if nilai >= 90:
                print("Akreditasi A")
            elif nilai >= 80:
                print("Akreditasi B")
            elif nilai >= 70:
                print("Akreditasi C")
            elif nilai >= 60:
                print("Akreditasi D")
            else:
                print("Nilai Anda kurang. Akreditasi E")
        except ValueError:
            print("Masukkan nilai yang valid.")

check_nilai()