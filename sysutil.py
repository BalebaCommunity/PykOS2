import customtkinter as ctk
import psutil
import platform

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class SystemMonitor(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Использование ПК")
        self.geometry("400x300")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame = ctk.CTkFrame(self, fg_color=("gray20", "gray10"))
        self.frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        self.label_cpu = ctk.CTkLabel(self.frame, text="Использование ЦП:", font=("Helvetica", 16))
        self.label_cpu.grid(row=0, column=0, sticky="w", pady=(0, 10))

        self.progressbar_cpu = ctk.CTkProgressBar(self.frame, progress_color=("light cyan", "light blue"))
        self.progressbar_cpu.grid(row=1, column=0, sticky="ew")

        self.label_cpu_text = ctk.CTkLabel(self.frame, text="", font=("Helvetica", 14))
        self.label_cpu_text.grid(row=1, column=1, sticky="w", padx=10)

        self.label_memory = ctk.CTkLabel(self.frame, text="Использование ОЗУ:", font=("Helvetica", 16))
        self.label_memory.grid(row=2, column=0, sticky="w", pady=(10, 0))

        self.progressbar_memory = ctk.CTkProgressBar(self.frame, progress_color=("pink", "light pink"))
        self.progressbar_memory.grid(row=3, column=0, sticky="ew")

        self.label_memory_text = ctk.CTkLabel(self.frame, text="", font=("Helvetica", 14))
        self.label_memory_text.grid(row=3, column=1, sticky="w", padx=10)

        self.label_disk = ctk.CTkLabel(self.frame, text="Использование места на диске:", font=("Helvetica", 16))
        self.label_disk.grid(row=4, column=0, sticky="w", pady=(10, 0))

        self.progressbar_disk = ctk.CTkProgressBar(self.frame, progress_color=("light gray", "gray"))
        self.progressbar_disk.grid(row=5, column=0, sticky="ew")

        self.label_disk_text = ctk.CTkLabel(self.frame, text="", font=("Helvetica", 14))
        self.label_disk_text.grid(row=5, column=1, sticky="w", padx=10)

        self.label_os = ctk.CTkLabel(self.frame, text="Операционная Система:", font=("Helvetica", 16))
        self.label_os.grid(row=6, column=0, sticky="w", pady=(10, 0))

        self.label_os_info = ctk.CTkLabel(self.frame, text=platform.system(), font=("Helvetica", 14))
        self.label_os_info.grid(row=7, column=0, sticky="w")

        self.update_system_info()

    def update_system_info(self):
        cpu_usage = psutil.cpu_percent(percpu=True)
        self.progressbar_cpu.set(max(cpu_usage) / 100)
        self.label_cpu_text.configure(text=f"{max(cpu_usage):.1f}%")

        memory_usage = psutil.virtual_memory().percent
        self.progressbar_memory.set(memory_usage / 100)
        self.label_memory_text.configure(text=f"{memory_usage:.1f}%")

        disk_usage = psutil.disk_usage('/').percent
        self.progressbar_disk.set(disk_usage / 100)
        self.label_disk_text.configure(text=f"{disk_usage:.1f}%")

        self.after(1000, self.update_system_info)

if __name__ == "__main__":
    app = SystemMonitor()
    app.mainloop()