from metaflow import FlowSpec, step

class KuliahInformatikaFlow(FlowSpec):

    @step
    def start(self):
        print("Mulai alur kuliah informatika.")
        self.next(self.bayar_spp_step)

    @step
    def bayar_spp_step(self):
        print("Langkah: Membayar SPP.")
        self.next(self.perkuliahan)  

    @step
    def perkuliahan(self):
        print("Langkah: Mengikuti perkuliahan.")
        self.next(self.tugas)  

    @step
    def tugas(self):
        print("Langkah: Mengerjakan tugas.")
        self.next(self.ujian)

    @step
    def ujian(self):
        print("Langkah: Mengikuti ujian.")
        self.next(self.KHS)  

    @step
    def KHS(self):
        print("Langkah: Mendapatkan KHS.")
        self.next(self.end)  

    @step
    def end(self):
        print("Flow selesai. Semua langkah sudah dijalankan.")

if __name__ == '__main__':
    KuliahInformatikaFlow()
