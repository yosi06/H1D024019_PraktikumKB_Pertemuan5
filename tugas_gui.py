import tkinter as tk
from tkinter import messagebox, scrolledtext

gejala = {
    "G1":  "Nafas abnormal",
    "G2":  "Suara serak",
    "G3":  "Perubahan kulit",
    "G4":  "Telinga penuh",
    "G5":  "Nyeri bicara menelan",
    "G6":  "Nyeri tenggorokan",
    "G7":  "Nyeri leher",
    "G8":  "Pendarahan hidung",
    "G9":  "Telinga berdenging",
    "G10": "Air liur menetes",
    "G11": "Perubahan suara",
    "G12": "Sakit kepala",
    "G13": "Nyeri pinggir hidung",
    "G14": "Serangan vertigo",
    "G15": "Getah bening",
    "G16": "Leher bengkak",
    "G17": "Hidung tersumbat",
    "G18": "Infeksi sinus",
    "G19": "Berat badan turun",
    "G20": "Nyeri telinga",
    "G21": "Selaput lendir merah",
    "G22": "Benjolan leher",
    "G23": "Tubuh tak seimbang",
    "G24": "Bola mata bergerak",
    "G25": "Nyeri wajah",
    "G26": "Dahi sakit",
    "G27": "Batuk",
    "G28": "Tumbuh di mulut",
    "G29": "Benjolan di leher",
    "G30": "Nyeri antara mata",
    "G31": "Radang gendang telinga",
    "G32": "Tenggorokan gatal",
    "G33": "Hidung meler",
    "G34": "Tuli",
    "G35": "Mual muntah",
    "G36": "Letih lesu",
    "G37": "Demam",
}

penyakit = {
    "Tonsilitis":               ["G37","G12","G5","G27","G6","G21"],
    "Sinusitis Maksilaris":     ["G37","G12","G27","G17","G33","G36","G29"],
    "Sinusitis Frontalis":      ["G37","G12","G27","G17","G33","G36","G21","G26"],
    "Sinusitis Etmoidalis":     ["G37","G12","G27","G17","G33","G36","G21","G30","G13","G26"],
    "Sinusitis Sfenoidalis":    ["G37","G12","G27","G17","G33","G36","G29","G7"],
    "Abses Peritonsiler":       ["G37","G12","G6","G15","G2","G29","G10"],
    "Faringitis":               ["G37","G5","G6","G7","G15"],
    "Kanker Laring":            ["G5","G27","G6","G15","G2","G19","G1"],
    "Deviasi Septum":           ["G37","G17","G20","G8","G18","G25"],
    "Laringitis":               ["G37","G5","G15","G16","G32"],
    "Kanker Leher & Kepala":    ["G5","G22","G8","G28","G3","G11"],
    "Otitis Media Akut":        ["G37","G20","G35","G31"],
    "Contact Ulcers":           ["G5","G2"],
    "Abses Parafaringeal":      ["G5","G16"],
    "Barotitis Media":          ["G12","G20"],
    "Kanker Nasofaring":        ["G17","G8"],
    "Kanker Tonsil":            ["G6","G29"],
    "Neuronitis Vestibularis":  ["G35","G24"],
    "Meniere":                  ["G20","G35","G14","G4"],
    "Tumor Saraf Pendengaran":  ["G12","G34","G23"],
    "Kanker Leher Metastatik":  ["G29"],
    "Otosklerosis":             ["G34","G9"],
    "Vertigo Postural":         ["G24"],
}

def diagnosa(gejala_pasien):
    hasil = []

    for nama_penyakit, gejala_penyakit in penyakit.items():
        cocok = [g for g in gejala_pasien if g in gejala_penyakit]
        jumlah_cocok = len(cocok)

        if jumlah_cocok > 0:
            persen = (jumlah_cocok / len(gejala_penyakit)) * 100
            hasil.append({
                "penyakit": nama_penyakit,
                "cocok": jumlah_cocok,
                "total": len(gejala_penyakit),
                "persen": persen,
                "gejala_cocok": cocok
            })

    hasil.sort(key=lambda x: x["persen"], reverse=True)
    return hasil

class AplikasiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SISTEM PAKAR DIAGNOSA PENYAKIT THT")
        self.root.geometry("850x750")
        self.root.configure(bg='#ecf0f1')

        self.buat_widget_input()
        self.buat_widget_output()
    
    def buat_widget_input(self):
        frame_input = tk.Frame(self.root, bg='#ecf0f1')
        frame_input.pack(pady=10, padx=10, fill='x')

        judul = tk.Label(frame_input, text="SISTEM PAKAR DIAGNOSA PENYAKIT THT", 
                         font=('Arial', 18, 'bold'), bg='#ecf0f1', fg='#2c3e50')
        judul.pack()
        
        subjudul = tk.Label(frame_input, text="(Telinga, Hidung, Tenggorokan)", 
                            font=('Arial', 11), bg='#ecf0f1', fg='#7f8c8d')
        subjudul.pack(pady=5)

        label_gejala = tk.Label(frame_input, text="Masukkan kode gejala (pisahkan dengan koma):", 
                                font=('Arial', 11), bg='#ecf0f1', fg='#2c3e50')
        label_gejala.pack(pady=(10,5))

        self.entry_gejala = tk.Entry(frame_input, font=('Arial', 12), width=55, 
                                      bg='white', fg='black', justify='center')
        self.entry_gejala.pack(pady=5)

        contoh = tk.Label(frame_input, text="Contoh: G1,G5,G12,G27", 
                          font=('Arial', 9), bg='#ecf0f1', fg='#7f8c8d')
        contoh.pack()

        frame_tombol = tk.Frame(frame_input, bg='#ecf0f1')
        frame_tombol.pack(pady=10)

        btn_diagnosa = tk.Button(frame_tombol, text="DIAGNOSA", command=self.proses_diagnosa,
                                 bg='#3498db', fg='white', font=('Arial', 11, 'bold'),
                                 padx=25, pady=5, cursor='hand2', width=12)
        btn_diagnosa.pack(side='left', padx=8)

        btn_reset = tk.Button(frame_tombol, text="RESET", command=self.reset,
                              bg='#e74c3c', fg='white', font=('Arial', 11, 'bold'),
                              padx=25, pady=5, cursor='hand2', width=12)
        btn_reset.pack(side='left', padx=8)

        btn_keluar = tk.Button(frame_tombol, text="KELUAR", command=self.root.quit,
                               bg='#95a5a6', fg='white', font=('Arial', 11, 'bold'),
                               padx=25, pady=5, cursor='hand2', width=12)
        btn_keluar.pack(side='left', padx=8)

        frame_daftar = tk.LabelFrame(frame_input, text=" DAFTAR GEJALA ", 
                                     font=('Arial', 12, 'bold'), bg='#ecf0f1', fg='#2c3e50')
        frame_daftar.pack(pady=10, fill='both', expand=True)

        text_gejala = tk.Text(frame_daftar, height=12, width=85, font=('Courier', 9), bg='#f9f9f9')
        scrollbar = tk.Scrollbar(frame_daftar, command=text_gejala.yview)
        text_gejala.configure(yscrollcommand=scrollbar.set)
        
        text_gejala.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        scrollbar.pack(side='right', fill='y')

        gejala_list = list(gejala.items())
        for i in range(0, len(gejala_list), 2):
            if i+1 < len(gejala_list):
                baris = f"  {gejala_list[i][0]:<5} - {gejala_list[i][1]:<25}     {gejala_list[i+1][0]:<5} - {gejala_list[i+1][1]}"
            else:
                baris = f"  {gejala_list[i][0]:<5} - {gejala_list[i][1]}"
            text_gejala.insert(tk.END, baris + "\n")
        text_gejala.configure(state='disabled')
    
    def buat_widget_output(self):
        frame_output = tk.LabelFrame(self.root, text=" HASIL DIAGNOSA ", 
                                     font=('Arial', 12, 'bold'), bg='#ecf0f1', fg='#2c3e50')
        frame_output.pack(pady=10, padx=10, fill='both', expand=True)

        self.text_hasil = scrolledtext.ScrolledText(frame_output, height=12, 
                                                      font=('Courier', 10), wrap=tk.WORD,
                                                      bg='#f9f9f9')
        self.text_hasil.pack(fill='both', expand=True, padx=5, pady=5)

        warning = tk.Label(frame_output, text="PERINGATAN: Hasil ini hanya perkiraan. Segera konsultasikan ke dokter THT!",
                           font=('Arial', 9, 'bold'), fg='red', bg='#ecf0f1')
        warning.pack(pady=5)
    
    def proses_diagnosa(self):
        inputan = self.entry_gejala.get().strip().upper()
        
        if not inputan:
            messagebox.showwarning("Peringatan", "Masukkan kode gejala terlebih dahulu!")
            return
        
        if inputan == "KELUAR":
            self.root.quit()
            return

        daftar_input = [g.strip() for g in inputan.split(",")]
        
        gejala_valid = []
        gejala_tidak_valid = []
        for g in daftar_input:
            if g in gejala:
                gejala_valid.append(g)
            else:
                gejala_tidak_valid.append(g)
        
        if gejala_tidak_valid:
            messagebox.showerror("Error", f"Kode tidak dikenal: {', '.join(gejala_tidak_valid)}")
            return
        
        if not gejala_valid:
            messagebox.showwarning("Peringatan", "Tidak ada kode gejala yang valid!")
            return

        self.text_hasil.delete(1.0, tk.END)
        
        self.text_hasil.insert(tk.END, "="*75 + "\n")
        self.text_hasil.insert(tk.END, "                     GEJALA YANG ANDA PILIH\n")
        self.text_hasil.insert(tk.END, "="*75 + "\n\n")
        for g in gejala_valid:
            self.text_hasil.insert(tk.END, f"   {g} : {gejala[g]}\n")
        
        hasil = diagnosa(gejala_valid)
        
        self.text_hasil.insert(tk.END, "\n" + "="*75 + "\n")
        self.text_hasil.insert(tk.END, "                      HASIL DIAGNOSA\n")
        self.text_hasil.insert(tk.END, "="*75 + "\n\n")
        
        if not hasil:
            self.text_hasil.insert(tk.END, "   Tidak ditemukan penyakit yang cocok.\n")
        else:
            for i, h in enumerate(hasil[:5], start=1):
                self.text_hasil.insert(tk.END, f"   {i}. {h['penyakit']}\n")
                self.text_hasil.insert(tk.END, f"      Kemiripan    : {h['persen']:.1f}% ({h['cocok']}/{h['total']} gejala cocok)\n")
                nama_gejala_cocok = [gejala[g] for g in h['gejala_cocok']]
                self.text_hasil.insert(tk.END, f"      Gejala cocok : {', '.join(nama_gejala_cocok)}\n\n")
        
        self.text_hasil.insert(tk.END, "="*75 + "\n")
        self.text_hasil.insert(tk.END, "PERINGATAN: Hasil ini hanya perkiraan.\n")
        self.text_hasil.insert(tk.END, "Segera konsultasikan ke dokter THT!\n")
        self.text_hasil.insert(tk.END, "="*75 + "\n")
    
    def reset(self):
        self.entry_gejala.delete(0, tk.END)
        self.text_hasil.delete(1.0, tk.END)

def main_gui():
    root = tk.Tk()
    app = AplikasiGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main_gui()