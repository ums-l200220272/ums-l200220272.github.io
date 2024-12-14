from metaflow import FlowSpec, step

class KuliahInformatikaFlow(FlowSpec):

    @step
    def start(self):
        print("\n=== Proses Mengikuti Kuliah di Informatika ===")
        self.bayar_spp = input("Apakah SPP sudah dibayar? (ya/tidak): ").lower() == "ya"
        self.next(self.bayar_spp_step)

    @step
    def bayar_spp_step(self):
        if not self.bayar_spp:
            print("SPP belum dibayar. Silakan bayar SPP terlebih dahulu!")
            self.next(self.end)
        else:
            print("SPP sudah dibayar. Anda bisa mengikuti perkuliahan.")
            self.next(self.perkuliahan)

    @step
    def perkuliahan(self):
        print("\n=== Mengikuti Perkuliahan ===")
        self.kehadiran = input("Apakah Anda mengikuti semua perkuliahan? (ya/tidak): ").lower() == "ya"
        if self.kehadiran:
            print("Anda telah mengikuti semua perkuliahan dengan baik.")
        else:
            print("Anda melewatkan beberapa perkuliahan. Ini bisa memengaruhi nilai akhir!")
        self.next(self.tugas)

    @step
    def tugas(self):
        print("\n=== Mengerjakan Tugas ===")
        jumlah_tugas = int(input("Berapa jumlah tugas yang harus dikerjakan? "))
        selesai = int(input("Berapa jumlah tugas yang sudah diselesaikan? "))
        self.tugas_selesai = selesai >= jumlah_tugas
        if self.tugas_selesai:
            print("Semua tugas telah selesai. Bagus sekali!")
        else:
            print("Ada tugas yang belum diselesaikan. Ayo kerjakan lagi!")
        self.next(self.ujian)

    @step
    def ujian(self):
        print("\n=== Mengikuti Ujian ===")
        self.nilai_ujian = float(input("Masukkan nilai ujian Anda (0-100): "))
        if self.nilai_ujian >= 60:
            print(f"Nilai ujian Anda adalah {self.nilai_ujian}. Anda lulus ujian!")
        else:
            print(f"Nilai ujian Anda adalah {self.nilai_ujian}. Anda tidak lulus ujian.")
        self.next(self.nilai_akhir)

    @step
    def nilai_akhir(self):
        print("\n=== Menghitung Nilai Akhir ===")
        bobot_kehadiran = 0.2
        bobot_tugas = 0.3
        bobot_ujian = 0.5

        # Konversi kehadiran dan tugas menjadi nilai
        nilai_kehadiran = 100 if self.kehadiran else 50
        nilai_tugas = 100 if self.tugas_selesai else 50

        # Menghitung nilai akhir
        self.nilai_akhir = (nilai_kehadiran * bobot_kehadiran) + (nilai_tugas * bobot_tugas) + (self.nilai_ujian * bobot_ujian)
        print(f"Nilai Akhir Anda adalah: {self.nilai_akhir:.2f}")

        if self.nilai_akhir >= 60:
            print("Selamat! Anda lulus mata kuliah ini.")
        else:
            print("Maaf, Anda belum lulus mata kuliah ini. Semangat untuk semester depan!")
        self.next(self.end)

    @step
    def end(self):
        print("\n=== Proses Selesai ===")
        if not self.bayar_spp:
            print("Harap bayar SPP agar dapat memulai perkuliahan.")
        else:
            print("Proses mengikuti kuliah telah selesai.")

if __name__ == "__main__":
    KuliahInformatikaFlow()
