import customtkinter as ctk
import tkinter as tk

class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Калькулятор")
        self.geometry("300x400")
        self.configure(bg="#3D3D3D")  # Более темный фон

        # Настройка стилей
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.display = ctk.CTkEntry(self, font=("Segoe UI", 20), justify="right", corner_radius=10)
        self.display.pack(padx=20, pady=20, fill="x")

        self.buttons_frame = ctk.CTkFrame(self, bg_color="#3D3D3D")
        self.buttons_frame.pack(padx=20, pady=10, fill="both", expand=True)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "C"
        ]

        row = 0
        col = 0
        for button_text in buttons:
            if button_text in ["+", "-", "*", "/", "=", "C"]:
                button_color = "#134648"
                text_color = "white"
            else:
                button_color = "#D8BAB1"
                text_color = "black"

            button = ctk.CTkButton(self.buttons_frame, text=button_text, font=("Segoe UI", 18),
                                   command=lambda x=button_text: self.click(x),
                                   bg_color=button_color, fg_color=button_color,
                                   text_color=text_color, hover_color="#A0A0A0",
                                   width=50, height=50)
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.buttons_frame.grid_rowconfigure(5, weight=1)
        for i in range(4):
            self.buttons_frame.grid_columnconfigure(i, weight=1)

    def click(self, key):
        if key == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, ctk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, ctk.END)
                self.display.insert(0, "Error")
        elif key == "C":
            self.display.delete(0, ctk.END)
        else:
            self.display.insert(ctk.END, key)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()